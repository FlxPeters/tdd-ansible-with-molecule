build:
	cp -r node_modules/reveal.js/dist/ docs/reveal.js; \
	cp -r node_modules/reveal.js/plugin/ docs/reveal.js; \
	node convert-slides.js