/* Purpose: synthetic article contracts; 2026-11-14; Branding. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {render,parse,buildIndex}=require('./renderArticle');
const sample='---\nstatus: draft\napproved: true\nbrand: personal\nformat: article\nslug: sistemas\ntitle: "Construir sistemas"\ndescription: "Uma reflexão."\n---\n## Contexto\nTexto sintético <script>alert(1)</script>.\n';
test('escapes text and emits canonical Portuguese article',()=>{const s=render(sample);assert.match(s,/lang="pt-BR"/);assert.match(s,/https:\/\/tailormaciel.com\/artigos\/sistemas.html/);assert.ok(!s.includes('<script>'));assert.match(s,/&lt;script&gt;/);});
test('refuses unapproved, wrong brand, blocked and traversal',()=>{for(const [a,b] of [['approved: true','approved: false'],['brand: personal','brand: fermac'],['status: draft','status: blocked'],['slug: sistemas','slug: ../x'],['slug: sistemas','slug: index']])assert.throws(()=>render(sample.replace(a,b)));});
test('rejects duplicate fields',()=>assert.throws(()=>parse(sample.replace('approved: true','approved: true\napproved: false'))));
test('index enumerates generated pages deterministically',()=>{const d=fs.mkdtempSync(path.join(os.tmpdir(),'personal-test-'));try{fs.writeFileSync(path.join(d,'sistemas.html'),render(sample));assert.equal(buildIndex(d),buildIndex(d));assert.match(buildIndex(d),/href="sistemas.html"/);assert.match(buildIndex(d),/Construir sistemas/);}finally{fs.rmSync(d,{recursive:true});}});

test('public HTTPS references are links; unsafe schemes remain text',()=>{const s=render(sample+'\n[Fonte](https://example.org/source) [Ataque](javascript:alert)');assert.match(s, /href="https:\/\/example.org\/source"/);assert.ok(!s.includes('href="javascript:'));});

test('missing required slug is refused rather than coerced to undefined',()=>assert.throws(()=>render(sample.replace('slug: sistemas\n',''))));
test('navbar compares resolved paths across root and nested indexes',()=>{
 const vm=require('node:vm'),code=fs.readFileSync(path.join(__dirname,'siteController.js'),'utf8');
 for(const [pathname,hrefs,expected] of [['/',['index.html','about.html','artigos/index.html'],[true,false,false]],['/index.html',['index.html','artigos/index.html'],[true,false]],['/about.html',['index.html','about.html','artigos/index.html'],[false,true,false]],['/artigos/',['../index.html','index.html'],[false,true]],['/artigos/index.html',['../index.html','index.html'],[false,true]]]){
  const links=hrefs.map(h=>({getAttribute:()=>h,active:true,classList:{toggle(_name,value){this.target.active=value;}}}));for(const l of links)l.classList.target=l;
  const context={URL,document:{getElementById:()=>({querySelectorAll:()=>links}),addEventListener:()=>{}},window:{location:{pathname,href:'https://tailormaciel.com'+pathname},addEventListener:()=>{}}};
  vm.createContext(context);vm.runInContext(code+'\nnew NavbarController();',context);assert.deepEqual(links.map(x=>x.active),expected,pathname);
 }
});

test('index and reading reuse full TM navigation, footer and controllers',()=>{
 const d=fs.mkdtempSync(path.join(os.tmpdir(),'tm-shell-'));
 try {for(const html of [render(sample),buildIndex(d)]){
  assert.match(html,/<a href="\.\.\/index.html" class="logo">TM<\/a>/);
  for(const target of ['about','experience','education','contact'])assert.match(html,new RegExp(`href="\\.\\./${target}\\.html"`));
  assert.match(html,/id="mobileMenuBtn"/);assert.match(html,/id="langToggle"/);
  assert.match(html,/<footer class="footer">/);assert.match(html,/footer__social/);
  assert.match(html,/\.\.\/translations\/strings.js/);assert.match(html,/\.\.\/scripts\/siteController.js/);
  assert.match(html,/aria-current="(?:page|true)" data-i18n="nav.articles"/);
 }}finally{fs.rmSync(d,{recursive:true});}
});
test('empty production index is reproducible and contains no demonstration',()=>{
 const d=path.join(__dirname,'../artigos');
 assert.ok(!fs.readdirSync(d).includes('demonstracao-visual.html'));
 assert.equal(fs.readFileSync(path.join(d,'index.html'),'utf8'),buildIndex(d));
 const empty=fs.mkdtempSync(path.join(os.tmpdir(),'tm-empty-'));
 try {assert.match(buildIndex(empty),/article-empty/);assert.doesNotMatch(buildIndex(empty),/article-card__link|demonstracao-visual/);}finally{fs.rmSync(empty,{recursive:true});}
});
test('readable hierarchy and references preserve escaped content and safe URLs',()=>{
 const html=render(sample+'\n### Um detalhe\nParágrafo um.\n\nParágrafo dois.\n\n## Referências\n- [Fonte](https://example.org/path?a=1&b=2)\n- [Privado](https://user:pass@example.org)');
 assert.match(html,/<h3>Um detalhe<\/h3>/);assert.match(html,/<p>Parágrafo um.<\/p>/);
 assert.match(html,/<section class="article-references">/);assert.match(html,/<ul>\s*<li>/);
 assert.match(html,/href="https:\/\/example.org\/path\?a=1&amp;b=2"/);
 assert.doesNotMatch(html,/href="https:\/\/user:/);
 assert.match(html,/class="article-prose" lang="pt-BR"/);
});
test('populated cards preserve entities once and do not interpret title HTML',()=>{
 const d=fs.mkdtempSync(path.join(os.tmpdir(),'tm-cards-'));
 try{
  fs.writeFileSync(path.join(d,'sistemas.html'),render(sample.replace('Construir sistemas','A & B <teste>')));
  const html=buildIndex(d);assert.match(html,/A &amp; B &lt;teste&gt;/);assert.doesNotMatch(html,/&amp;amp;|<teste>/);
  assert.match(html,/data-i18n="articles.read"/);
 }finally{fs.rmSync(d,{recursive:true});}
});
test('preview prepares demo and empty states outside the production tree',()=>{
 const {preparePreview}=require('./previewArticles');const d=preparePreview();
 try{
  assert.ok(!d.startsWith(path.resolve(__dirname,'..')+path.sep));
  assert.ok(fs.existsSync(path.join(d,'artigos/demonstracao-visual.html')));
  assert.doesNotMatch(fs.readFileSync(path.join(d,'_states/empty/artigos/index.html'),'utf8'),/demonstracao-visual/);
  for(const name of ['.git','README.md','scripts/renderArticle.js','scripts/previewArticles.js'])assert.ok(!fs.existsSync(path.join(d,name)));
 }finally{fs.rmSync(d,{recursive:true});}
});
