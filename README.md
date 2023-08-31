# Pipeline de ETL com Python

### Esse repositório foi desenvolvido para um dos projetos do bootcamp Santander da DIO.


#### Projeto

O cliente possue 2 arquivos em formatos CSV e precisa que seja gerado um terceiro aquivo unindo esses arquivos.


[Users]('/data/destinys.csv')
> Nesse arquivo temos os usuários e os IDs das cidades que eles vão viajar

[Destiny]('/data/destinys.csv')
> Nesse arquivos temos os IDs das cidades e seus pontos turisticos.


### Solução

Após a ETL é gerado o arquivo [Travelers]('/data/travelers.csv') que é a junção dos dois arquivos anteriores unindo cada usuário com a cidade para onde está viajando e um ponto turistico daquela cidade.

