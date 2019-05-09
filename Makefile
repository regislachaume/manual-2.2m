file:
	pdflatex operation-manual
	makeglossaries operation-manual
	pdflatex operation-manual
	pdflatex operation-manual

publish:
	make file
	/home/lachaume/bin/mpgcopymanual
