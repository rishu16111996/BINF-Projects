#!/usr/bin/env bash
#renderMethods.sh
R -e "rmarkdown::render('methods.Rmd', output_format='md_document')"
