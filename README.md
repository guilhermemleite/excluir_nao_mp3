# Script para excluir arquivos não .mp3 com segurança

Este script em Python exclui todos os arquivos que não sejam da extensão .mp3 em uma pasta e suas subpastas, movendo-os para a lixeira em vez de excluí-los permanentemente. Ele é ideal para organizar diretórios de mídia, mantendo apenas arquivos .mp3 e garantindo a segurança de exclusão, caso algum arquivo seja movido para a lixeira por engano.

Como funciona:

O script segue as etapas abaixo:

1. Interação com o usuário:

- Solicita o caminho de uma pasta para realizar o processo.
- Após o processamento, pergunta se o usuário deseja repetir o procedimento em outra pasta ou encerrar.

2. Verificação de arquivos:

- Identifica todos os arquivos na pasta principal e em suas subpastas.
- Verifica se o arquivo tem extensão .mp3 (ignora maiúsculas e minúsculas).

3. Movimento seguro:

- Arquivos que não são .mp3 são movidos para a lixeira usando a biblioteca send2trash, garantindo que possam ser recuperados, se necessário.

4. Conclusão do processo:

- Após concluir o processamento, exibe uma lista dos arquivos que foram movidos para a lixeira e permite ao usuário processar outra pasta ou encerrar o programa.


Estrutura do código

1. Função excluir_nao_mp3:

- Percorre os diretórios com os.walk().
- Identifica arquivos que não possuem a extensão .mp3.
- Move esses arquivos para a lixeira usando send2trash.

2. Função main:

- Solicita ao usuário o caminho da pasta.
- Chama a função de exclusão e gerencia o fluxo do programa.
- Oferece a opção de repetir o processo em outra pasta ou encerrar o programa.

3. Biblioteca send2trash:

- Utilizada para mover arquivos para a lixeira em vez de excluí-los permanentemente.


Pré-requisitos

1. Python 3.6 ou Superior:

- O script utiliza recursos modernos da linguagem.

2. Biblioteca send2trash:

- Instale com o comando:
pip install send2trash



