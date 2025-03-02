# Sumário
O objetivo deste exercício foi processar um dicionário médico em formato de texto e transformá-lo num arquivo HTML, onde cada conceito aparece acima da respetiva descrição, sem erros de formatação.

# Decisões de Implementação

## 1.
Percorrer o texto e encontrar todas as ocorrências de duas quebras de linha consecutivas, mas apenas se não forem seguidas por uma quebra de página. Cada uma das ocorrências é então substituída por duas quebras de linha seguidas de um @.
O objetivo foi criar uma marcação para separar os conceitos no dicionário.

## 2.
Remover todas as ocorrências de quebras de página (\f).

## 3.
Limpar a descrição removendo os @, eliminando espaços extras e ajustando o formato.

## 4.
Usar uma expressão regular para extrair os conceitos e descrições do texto e, em seguida, limpar cada descrição (removendo os @ e ajustando os espaços) antes de armazená-las numa lista chamada conceitos onde cada elemento é uma tupla, em que o primeiro valor é o nome do conceito (designação) e o segundo é a descrição limpa.

## 5.
Criar o html e inserir-lhe informação.

## Desafios encontrados
Durante o desenvolvimento do código, foram feitas várias tentativas de extração dos conceitos e descrições usando expressões regulares, mas todas apresentaram problemas. Algumas das tentativas não conseguiram capturar corretamente todos os conceitos. Outras não permitiram extrair as descrições completas, especialmente quando elas apresentavam várias linhas, resultando em corte de texto. E ainda houve uma tentativa, que utilizava o modificador re.DOTALL para capturar múltiplas linhas, que funcionou mas não era dessa maneira que eu queria resolver o problema.
