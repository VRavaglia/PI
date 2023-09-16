# BuscaPC

Trabalho da disciplina de Projeto Integrado - Engenharia Eletrônica UFRJ 2020.2

Quando um consumidor acessa um site de um varejista que oferece a venda de componentes para computador, o mesmo tem acesso a informações que podem não estar padronizadas ou que não estão arrumadas de maneira adequada. Além disso, normalmente esses sites não trazem informações acerca de compatibilidade de produtos, o que pode causar inconveniências ao comprador. Nos propomos a implementação de um site que oferece uma melhor organização das informações relevantes para cada produto, além da implementação de um sistema que checa essas compatibilidades. No geral, o desenvolvimento do sistema foi bem-sucedido, sendo o protótipo desenvolvido capaz de oferecer as funcionalidades prometidas no início desse projeto. 

# Solução Proposta

Com o objetivo de facilitar a escolha de componentes na compra de um computador desktop propomos uma interface web. Essa ferramenta agrega as peças de dois sites diferentes e extrai as especificações interessantes para a tomada de decisão no momento da compra. A proposta segue o seguinte fluxograma:

![flux](https://i.imgur.com/XegatcY.png)

A plataforma proposta pode ser dividida em três componentes básicos: o webscraping, feito com [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/); o banco de dados, feito com [SQLite](https://www.sqlite.org/index.html); e a interface web, que por sua vez é divida em um backend com [Node JS](https://nodejs.org/en) e frontend com [Vue JS](https://vuejs.org/). O funcionamento geral da aplicação se inicia na extração de informações relevantes de produtos contidos em dois sites especializados em componentes de computador. Em seguida, essas informações são interpretadas, filtradas e armazenadas em um banco de dados. E finalmente, uma interface web tem acesso ao banco de dados e permite ao usuário pesquisar por peças com as especificações já filtradas.
