build:
	cp -r node_modules/reveal.js/dist/ dist/reveal.js; \
	cp -r node_modules/reveal.js/plugin/ dist/reveal.js; \
	node convert-slides.js