## Expressões matemáticas do Word para RMarkdown utilizando regex

Este script foi feito para converter equações escritas no Word para uma formatação que o RMarkdown reconhecesse. 

Sendo 80 equações a serem convertidas, optei por escrever esse script para evitar o trabalho manual e também praticar o uso de Regex.

As equações são do exercício 6 do Módulo 9 da disciplina de Processamento de Sinais Biomédicos

Foram reconhecidos 5 padrões:
- Padrão 1 (W\d{2}x)') 
- Padrão 2 (W\d{2}\(x)') 
- Padrão 3 (W\d{3})')
- Padrão 4 (W\d{3}[A-Z])')
- Padrão 5 (W\d{2}[A-Z])')

### Exemplo de expressão do tipo 1:

 - A = x(0) + W20x(2)

$$ A = x(0) + W_2^0x(2) $$

### Exemplo de expressão do tipo 2:
- W80(x

$$ W_8^0(x $$

### Exemplo de expressão do tipo 3:
- W165

$$ W_{16}^5 $$

### Exemplo de expressão do tipo 4:
- X(0) = A2 + W160I2

$$ X(0) = A2 + W_{16}^0I2  $$

### Exemplo de expressão do tipo 5:
- A2 = A1 + W80E1

$$ A2 = A1 + W_8^0E1  $$

Ao final, os resultados são printados no console e também exportados pra um .txt. O texto pode ser diretamente colado no RMarkdown para que as equações sejam mostradas adequadamente.
