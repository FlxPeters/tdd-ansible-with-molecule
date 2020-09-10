#!/bin/bash

while inotifywait -e close_write index.adoc; do 
  (bundle exec asciidoctor-revealjs -a revealjsdir=https://cdn.jsdelivr.net/npm/reveal.js@3.9.2 index.adoc)
done


