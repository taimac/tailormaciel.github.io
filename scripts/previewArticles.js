#!/usr/bin/env node
/* Purpose: isolated visual preview; 2026-11-14; Branding. No production writes. */
'use strict';
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const http = require('node:http');
const {render, buildIndex} = require('./renderArticle');
const root = path.resolve(__dirname, '..');
const demo = `---
status: draft
approved: true
brand: personal
format: article
slug: demonstracao-visual
title: "Da pergunta ao sistema: um exemplo de leitura"
description: "Um artigo sintético para avaliar título, introdução, corpo e referências dentro da identidade do portfólio."
---
Este texto é uma demonstração visual. Não é um artigo publicado nem um relato de trabalho de Tailor Maciel. Ele existe apenas nesta prévia para testar o percurso de leitura.

## Começar por uma boa pergunta
Antes de escolher uma ferramenta, vale descrever a situação que precisa melhorar. Uma pergunta concreta ajuda a organizar o raciocínio e a reconhecer o que ainda precisa ser entendido.

O espaço entre os parágrafos, a largura da coluna e o contraste devem tornar a leitura confortável. Aqui, o conteúdo é propositalmente simples: o objetivo é avaliar a apresentação, sem antecipar uma publicação real.

### Transformar observação em estrutura
Uma sequência curta permite experimentar listas e subtítulos sem perder o fio da leitura:
- Registrar a pergunta e o contexto.
- Distinguir o que foi observado do que ainda é hipótese.
- Testar uma melhoria pequena e rever o resultado.

## Voltar ao contexto
Uma página de leitura também faz parte de um site. A marca, os caminhos de navegação e o rodapé ajudam quem chegou diretamente ao artigo a conhecer o restante do trabalho.

As referências ficam separadas do corpo, com links visíveis e espaço para títulos longos. O texto permanece em português quando os controles da interface mudam de idioma.

## Referências
- [MDN — Fundamentos de HTML](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/Structuring_content)
- [W3C — Introdução à acessibilidade na web](https://www.w3.org/WAI/fundamentals/accessibility-intro/)
`;
function copyPublic(destination) {
 fs.mkdirSync(destination, {recursive:true});
 for (const name of ['index.html','about.html','experience.html','education.html','contact.html','styles','images','translations','artigos']) {
  fs.cpSync(path.join(root,name),path.join(destination,name),{recursive:true});
 }
 fs.mkdirSync(path.join(destination,'scripts'));
 fs.copyFileSync(path.join(root,'scripts/siteController.js'),path.join(destination,'scripts/siteController.js'));
}
function preparePreview() {
 const directory = fs.mkdtempSync(path.join(os.tmpdir(),'tm-artigos-preview-'));
 copyPublic(directory);
 copyPublic(path.join(directory,'_states/empty'));
 fs.writeFileSync(path.join(directory,'artigos/demonstracao-visual.html'),render(demo));
 fs.writeFileSync(path.join(directory,'artigos/index.html'),buildIndex(path.join(directory,'artigos')));
 return directory;
}
function serve(directory, port=8787) {
 const types={'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml','.png':'image/png','.jpeg':'image/jpeg','.jpg':'image/jpeg'};
 const server=http.createServer((req,res)=>{
  let target;
  try {
   const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
   target=path.resolve(directory,'.'+pathname);
   if(!target.startsWith(directory+path.sep)&&target!==directory)throw Error();
   if(fs.statSync(target).isDirectory())target=path.join(target,'index.html');
   if(!types[path.extname(target)]||!fs.statSync(target).isFile())throw Error();
  } catch {res.writeHead(404);res.end('Not found');return;}
  res.writeHead(200,{'Content-Type':types[path.extname(target)],'Cache-Control':'no-store','X-Robots-Tag':'noindex, nofollow'});
  fs.createReadStream(target).pipe(res);
 });
 server.listen(port,'127.0.0.1',()=>console.log(JSON.stringify({url:`http://127.0.0.1:${server.address().port}/`,empty:`http://127.0.0.1:${server.address().port}/_states/empty/artigos/`,directory})));
 return server;
}
if(require.main===module) {
 const port=Number(process.argv[2]||8787);
 if(!Number.isInteger(port)||port<1024||port>65535)throw Error('port must be 1024–65535');
 serve(preparePreview(),port);
}
module.exports={preparePreview,serve,demo};
