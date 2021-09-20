// Load Asciidoctor.js and the reveal.js converter
var asciidoctor = require('@asciidoctor/core')()
var asciidoctorRevealjs = require('@asciidoctor/reveal.js')
asciidoctorRevealjs.register()

// Convert the document 'index.adoc' using the reveal.js converter
var attributes = {'revealjsdir': 'reveal.js'};
var options = { safe: 'safe', backend: 'revealjs',attributes: attributes, to_dir: "dist" }
asciidoctor.convertFile('index.adoc', options)