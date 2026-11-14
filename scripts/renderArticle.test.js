/* Purpose: synthetic article contracts; 2026-11-14; Branding. */
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),os=require('node:os'),path=require('node:path');
const {render,parse,buildIndex}=require('./renderArticle');
const sample='---\nstatus: draft\napproved: true\nbrand: personal\nformat: article\nslug: sistemas\ntitle: "Construir sistemas"\ndescription: "Uma reflexão."\n---\n## Contexto\nTexto sintético <script>alert(1)</script>.\n';
test('escapes text and emits canonical Portuguese article',()=>{const s=render(sample);assert.match(s,/lang="pt-BR"/);assert.match(s,/https:\/\/tailormaciel.com\/artigos\/sistemas.html/);assert.ok(!s.includes('<script>'));assert.match(s,/&lt;script&gt;/);});
test('refuses unapproved, wrong brand, blocked and traversal',()=>{for(const [a,b] of [['approved: true','approved: false'],['brand: personal','brand: fermac'],['status: draft','status: blocked'],['slug: sistemas','slug: ../x'],['slug: sistemas','slug: index']])assert.throws(()=>render(sample.replace(a,b)));});
test('rejects duplicate fields',()=>assert.throws(()=>parse(sample.replace('approved: true','approved: true\napproved: false'))));
test('index enumerates generated pages deterministically',()=>{const d=fs.mkdtempSync(path.join(os.tmpdir(),'personal-test-'));try{fs.writeFileSync(path.join(d,'sistemas.html'),render(sample));assert.equal(buildIndex(d),buildIndex(d));assert.match(buildIndex(d),/href="sistemas.html"/);assert.match(buildIndex(d),/Construir sistemas/);}finally{fs.rmSync(d,{recursive:true});}});

test('public HTTPS references are links; unsafe schemes remain text',()=>{const s=render(sample+'\n[Fonte](https://example.org/source) [Ataque](javascript:alert)');assert.match(s, /href="https:\/\/example.org\/source"/);assert.ok(!s.includes('href="javascript:'));});
