file:
	pdflatex operation-manual
	makeglossaries operation-manual
	pdflatex operation-manual
	pdflatex operation-manual

publish:
	scp operation-manual.pdf lachaume@black.astro.puc.cl:.www/2.2m/operations/operation-manual.pdf
