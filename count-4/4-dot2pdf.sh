dot -Tps 4-graphviz-example1.dot -o 4-graphviz-example1.ps
ps2pdf 4-graphviz-example1.ps 4-graphviz-example1.pdf

dot -Tps 4-graphviz-example2.dot -o 4-graphviz-example2.ps
ps2pdf 4-graphviz-example2.ps 4-graphviz-example2.pdf

python 4-grammar_to_graphviz.py < grammar > grammar.dot
dot -Tgif grammar.dot -o grammar.gif
