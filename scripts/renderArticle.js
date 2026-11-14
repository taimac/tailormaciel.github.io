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
/** Reuse the portfolio's own chrome; a missing reference is a build error. */
function portfolioChrome(index=false) {
 const reference=fs.readFileSync(path.join(root,'about.html'),'utf8');
 const nav=reference.match(/<nav class="navbar"[\s\S]*?<\/nav>/)?.[0];
 const footer=reference.match(/<footer class="footer">[\s\S]*?<\/footer>/)?.[0];
 if(!nav||!footer) throw Error('portfolio navigation/footer reference missing');
 const nested=html=>html.replace(/href="(index\.html|about\.html|experience\.html|education\.html|contact\.html|artigos\/index\.html)"/g,(_all,target)=>`href="${target==='artigos/index.html'?'index.html':'../'+target}"`)
  .replace(/(<a href="index\.html")(?! data-i18n)/g,'$1 data-i18n="nav.articles"');
 return {nav:nested(nav).replace('<a href="index.html" data-i18n="nav.articles"',`<a href="index.html" aria-current="${index?'page':'true'}" data-i18n="nav.articles"`),footer:nested(footer)};
}
function shell(title, description, content, canonical, index=false) {
 const {nav,footer}=portfolioChrome(index);
 return `<!DOCTYPE html>
<!-- Purpose: generated Artigos page; Date: 2026-11-14; Author: Codex for Tailor Maciel; Domain: Branding -->
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title${index?' data-i18n="articles.pageTitle"':''}>${esc(title)} — Tailor Maciel</title>
    <meta name="description" content="${esc(description)}">
    <meta name="author" content="Tailor Maciel">
    <link rel="canonical" href="https://tailormaciel.com/artigos/${canonical}">
    <link rel="stylesheet" href="../styles/pages/main.css?v=20260507-mobile-pass">
    <link rel="stylesheet" href="../styles/pages/articles.css?v=20261114-identity">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body class="articles-page${index?' articles-index':' article-reading'}">
    <a class="article-skip" href="#conteudo" data-i18n="articles.skip">Ir para o conteúdo</a>
    ${nav}
    <main id="conteudo" tabindex="-1">
${content}
    </main>
    ${footer}
    <script src="../translations/strings.js?v=20261114-articles"></script>
    <script src="../scripts/siteController.js?v=20261114-articles-focus"></script>
</body>
</html>\n`;
}
function renderBody(body) {
 let html='', paragraphs=[], list=false;
 const paragraph=()=>{if(paragraphs.length){html+=`<p>${inline(paragraphs.join(' '))}</p>\n`;paragraphs=[];}};
 const endList=()=>{if(list){html+='</ul>\n';list=false;}};
 let references=false;
 for(const line of body.split(/\r?\n/)) {
  const heading=/^(#{2,3})\s+(.+)$/.exec(line);
  const item=/^[-*]\s+(.+)$/.exec(line);
  if(heading){
   paragraph();endList();
   if(references){html+='</section>\n';references=false;}
   const level=heading[1].length;
   if(level===2&&/^(referências|references|fontes)$/i.test(heading[2].trim())){html+='<section class="article-references">\n';references=true;}
   html+=`<h${level}>${esc(heading[2])}</h${level}>\n`;
  } else if(item){paragraph();if(!list){html+='<ul>\n';list=true;}html+=`<li>${inline(item[1])}</li>\n`;}
  else if(!line.trim()){paragraph();endList();}
  else {endList();paragraphs.push(line.trim());}
 }
 paragraph();endList();if(references)html+='</section>\n';
 if(!html.trim())throw Error('empty article');
 return html;
}
function render(text) {
 const {meta,body}=parse(text);
 const content=`        <article>
            <header class="page-hero article-hero">
                <div class="page-hero__content">
                    <a class="article-back" href="index.html"><span aria-hidden="true">←</span> <span data-i18n="articles.back">Todos os artigos</span></a>
                    <h1 class="page-hero__title article-hero__title" lang="pt-BR">${esc(meta.title)}</h1>
                    <p class="page-hero__subtitle article-lead" lang="pt-BR">${esc(meta.description)}</p>
                    <div class="article-meta"><span data-i18n="articles.byline">Por Tailor Maciel</span><span aria-hidden="true">·</span><span data-i18n="articles.language">Artigo em português</span></div>
                </div>
            </header>
            <div class="article-prose" lang="pt-BR">
${renderBody(body)}
            </div>
        </article>
        <nav class="article-return" aria-label="Continuar a leitura" data-i18n-aria="articles.continueAria">
            <a href="index.html" class="btn-outline"><span aria-hidden="true">←</span> <span data-i18n="articles.back">Todos os artigos</span></a>
            <a href="../experience.html" data-i18n="articles.explore">Conhecer meu trabalho</a>
        </nav>`;
 return shell(meta.title,meta.description,content,`${meta.slug}.html`);
}
function decodeEntities(text) {
 const values={'&amp;':'&','&lt;':'<','&gt;':'>','&quot;':'"','&#39;':"'"};
 return text.replace(/&(?:amp|lt|gt|quot|#39);/g,m=>values[m]);
}
function buildIndex(directory) {
 const pages=fs.readdirSync(directory).filter(n=>/^[a-z0-9]+(?:-[a-z0-9]+)*\.html$/.test(n)&&n!=='index.html').sort();
 const cards=pages.map(n=>{
  const html=fs.readFileSync(path.join(directory,n),'utf8');
  const title=/<h1(?:\s[^>]*)?>([\s\S]*?)<\/h1>/.exec(html)?.[1];
  const description=/<meta name="description" content="([^"]*)"/.exec(html)?.[1]||'';
  if(!title)throw Error('article title missing');
  return `                    <li><article class="article-card"><a class="article-card__link" href="${esc(n)}">
                        <span class="article-card__type" data-i18n="articles.type">Artigo</span>
                        <h2 lang="pt-BR">${esc(decodeEntities(title))}</h2>
                        <p lang="pt-BR">${esc(decodeEntities(description))}</p>
                        <span class="article-card__read"><span data-i18n="articles.read">Ler artigo</span><span aria-hidden="true">↗</span></span>
                    </a></article></li>`;
 }).join('\n');
 const empty=`            <div class="article-empty">
                <div class="article-empty__mark" aria-hidden="true"><svg viewBox="0 0 48 48" fill="none"><path d="M13 8h16l7 7v25H13V8Z" stroke="currentColor" stroke-width="2"/><path d="M29 8v8h7M20 24h10M20 30h10" stroke="currentColor" stroke-width="2"/></svg></div>
                <span class="eyebrow" data-i18n="articles.emptyEyebrow">Um espaço em construção</span>
                <h2 data-i18n="articles.emptyTitle">As próximas ideias estão em preparação.</h2>
                <p data-i18n="articles.emptyText">Os artigos aparecerão aqui depois de revisados. Enquanto isso, conheça os projetos e experiências que dão origem a essa escrita.</p>
                <a href="../experience.html" class="btn-outline"><span data-i18n="articles.explore">Conhecer meu trabalho</span><span aria-hidden="true">→</span></a>
            </div>`;
 const content=`        <header class="page-hero articles-hero">
            <div class="page-hero__content">
                <span class="eyebrow" data-i18n="articles.eyebrow">Negócios · Tecnologia · Sistemas</span>
                <h1 class="page-hero__title" data-i18n="articles.title">Artigos</h1>
                <p class="page-hero__subtitle" data-i18n="articles.intro">Reflexões sobre o que acontece quando experiência comercial encontra tecnologia — e vira conhecimento compartilhado.</p>
            </div>
        </header>
        <section class="articles-collection" aria-label="Artigos publicados" data-i18n-aria="articles.listAria">
${pages.length?`            <div class="articles-collection__heading"><h2 data-i18n="articles.collectionTitle">Para ler com calma</h2><span class="article-count">${pages.length} <span data-i18n="${pages.length===1?'articles.countOne':'articles.countMany'}">${pages.length===1?'artigo':'artigos'}</span></span></div>
            <ul class="article-grid">
${cards}
            </ul>`:empty}
        </section>`;
 return shell('Artigos','Reflexões sobre negócios, tecnologia e construção de sistemas.',content,'index.html',true);
}
if(require.main===module) {
 try {const args=process.argv.slice(2);if(args.length!==1)throw Error('usage: node scripts/renderArticle.js article.md');const text=fs.readFileSync(args[0],'utf8');const {meta}=parse(text);const dir=path.join(root,'artigos');fs.mkdirSync(dir,{recursive:true});const out=path.join(dir,meta.slug+'.html');if(fs.existsSync(out))throw Error('article already exists');fs.writeFileSync(out,render(text),{flag:'wx'});fs.writeFileSync(path.join(dir,'index.html'),buildIndex(dir));}catch(e){console.error(e.message);process.exitCode=1;}
}
module.exports={parse,render,buildIndex,portfolioChrome};
