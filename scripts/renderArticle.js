#!/usr/bin/env node
/* Purpose: approved Portuguese article renderer; 2026-11-14; Branding; personal site. */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
function inline(text) {
 let result='', last=0;
 for(const m of text.matchAll(/\[([^\]]+)\]\((https:\/\/[^\s()]+)\)/g)) {
  result+=esc(text.slice(last,m.index));
  let valid=false;
  try {const u=new URL(m[2]);valid=u.protocol==='https:'&&!u.username&&!u.password;}catch{}
  result+=valid?`<a href="${esc(m[2])}">${esc(m[1])}</a>`:esc(m[0]);
  last=m.index+m[0].length;
 }
 return result+esc(text.slice(last));
}
function parse(text) {
 const m = /^---\r?\n([\s\S]*?)\r?\n---\r?\n/.exec(text);
 if (!m) throw Error('frontmatter required');
 const meta = Object.create(null);
 for (const line of m[1].split(/\r?\n/)) {
  if (!line.trim() || line.trim().startsWith('#')) continue;
  const pair = /^([a-z_]+):\s*(.*)$/.exec(line);
  if (!pair || Object.hasOwn(meta,pair[1])) throw Error('invalid or duplicate field');
  let value=pair[2];
  if (value.startsWith('"')) value=JSON.parse(value);
  else if (value.startsWith("'")) { if(!value.endsWith("'")) throw Error('invalid string'); value=value.slice(1,-1).replace(/''/g,"'"); }
  meta[pair[1]]=value;
 }
 if(meta.approved!=='true' || meta.brand!=='personal' || meta.format!=='article' || !['draft','approved'].includes(meta.status)) throw Error('approved personal article required');
 if(typeof meta.slug!=='string' || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(meta.slug) || meta.slug==='index') throw Error('invalid slug');
 if(!meta.title?.trim() || !meta.description?.trim()) throw Error('title and description required');
 return {meta,body:text.slice(m[0].length)};
}
function shell(title, description, content, canonical) {
 return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(title)} — Tailor Maciel</title><meta name="description" content="${esc(description)}"><link rel="canonical" href="https://tailormaciel.com/artigos/${canonical}"><link rel="stylesheet" href="../styles/pages/main.css"><style>main{max-width:760px;margin:7rem auto 4rem;padding:0 1.25rem;line-height:1.8}nav{padding:1rem;display:flex;gap:1.5rem}article h2{margin-top:2.5rem}article p{margin:1.25rem 0}a{overflow-wrap:anywhere}</style></head><body><a href="#conteudo">Ir para o conteúdo</a><nav aria-label="Navegação"><a href="../index.html">TM · Início</a><a href="index.html">Artigos</a><a href="../contact.html">Contato</a></nav><main id="conteudo">${content}</main><footer><p>© Tailor Maciel</p></footer></body></html>\n`;
}
function render(text) {
 const {meta,body}=parse(text); let html='', para=[];
 const flush=()=>{if(para.length){html+=`<p>${inline(para.join(' '))}</p>`;para=[];}};
 for(const line of body.split(/\r?\n/)) {
  const h=/^(#{2,3})\s+(.+)$/.exec(line);
  if(h){flush();const level=h[1].length;html+=`<h${level}>${esc(h[2])}</h${level}>`;}
  else if(!line.trim()) flush(); else para.push(line.trim());
 }
 flush(); if(!html.trim()) throw Error('empty article');
 return shell(meta.title,meta.description,`<article><h1>${esc(meta.title)}</h1>${html}</article>`,`${meta.slug}.html`);
}
function buildIndex(directory) {
 const pages=fs.readdirSync(directory).filter(n=>/^[a-z0-9]+(?:-[a-z0-9]+)*\.html$/.test(n)&&n!=='index.html').sort();
 const links=pages.map(n=>{const html=fs.readFileSync(path.join(directory,n),'utf8');const title=/<h1>([\s\S]*?)<\/h1>/.exec(html)?.[1];if(!title) throw Error('article title missing');return `<li><a href="${esc(n)}">${title}</a></li>`;}).join('');
 return shell('Artigos','Reflexões sobre negócios, tecnologia e construção de sistemas.',`<h1>Artigos</h1>${pages.length?`<ul>${links}</ul>`:'<p>Os próximos artigos serão publicados aqui após revisão.</p>'}`,'index.html');
}
if(require.main===module) {
 try {const args=process.argv.slice(2);if(args.length!==1)throw Error('usage: node scripts/renderArticle.js article.md');const text=fs.readFileSync(args[0],'utf8');const {meta}=parse(text);const dir=path.join(root,'artigos');fs.mkdirSync(dir,{recursive:true});const out=path.join(dir,meta.slug+'.html');if(fs.existsSync(out))throw Error('article already exists');fs.writeFileSync(out,render(text),{flag:'wx'});fs.writeFileSync(path.join(dir,'index.html'),buildIndex(dir));}catch(e){console.error(e.message);process.exitCode=1;}
}
module.exports={parse,render,buildIndex};
