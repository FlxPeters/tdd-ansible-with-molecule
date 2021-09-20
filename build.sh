#!/bin/bash

while inotifywait -e close_write index.adoc; do 
  node convert-slides.js
done


