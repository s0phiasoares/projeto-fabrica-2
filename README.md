
# 💼 Calculadora de Salário Mensal

Um mini-projeto em **Python** que calcula o **salário total do mês** a partir do **valor da hora** e do **número de horas trabalhadas** no período. Foco em praticar **entrada de dados**, **validação**, **operações matemáticas** e **formatação de saída**.

---

## 🎯 Objetivo Educacional
- Reforçar o fluxo **entrada → processamento → saída**.
- Usar `input()`, conversão para `float`, validação de faixas e **f-strings**.
- Introduzir **funções puras** e testes com `unittest`.

---

## 📝 Enunciado
Você foi convidado a desenvolver uma **Calculadora de Salário Mensal** para sua turma. Seu programa deve:
1. Perguntar **quanto você ganha por hora** (ex.: 25.50).
2. Perguntar **quantas horas trabalhou no mês** (ex.: 160).
3. Calcular o salário do mês (**valor_hora × horas**).
4. Exibir o resultado com **2 casas decimais**.

> Exemplo
```
Digite quanto você ganha por hora: 25.50
Digite o número de horas trabalhadas no mês: 160

Seu salário do mês é: R$ 4080.00
```

---

## 💻 Como executar

Pré-requisito: **Python 3.8+**

1) Clone este repositório ou baixe os arquivos.
```bash
git clone https://github.com/seu-usuario/projeto-fabrica-2.git
cd projeto-fabrica-2
```

2) Rode o programa:
```bash
python salario.py
```

3) Informe **valor da hora** e **horas trabalhadas** quando solicitado. 🎉

> Dica (Windows): se `python` não funcionar, tente `py salario.py`.

---

## 🧪 (Opcional) Rodando testes
Sem dependências externas. Use o `unittest` padrão:
```bash
python -m unittest
```

---

## 🧠 Conceitos trabalhados
- Entrada com `input()` e conversão para `float`
- Validação de faixas (valores não negativos; limite razoável para horas)
- Funções puras (`calcular_salario`) e funções de I/O (`ler_valor`, `ler_horas`)
- Formatação com f-strings
- Organização de projeto + README

---

## 🚀 Extensões sugeridas
- Calcular **salário bruto**, **descontos** (INSS, IR) e **salário líquido**.
- Aceitar **carga horária semanal** e calcular horas do mês automaticamente.
- Interface gráfica simples com **Tkinter** ou **Streamlit**.
- Internacionalização (mensagens em **pt**/**en**).

---

## 📂 Estrutura do projeto
```
calculadora-salario-mensal/
├─ salario.py
├─ README.md
├─ tests/
│  └─ test_salario.py
├─ .gitignore
└─ LICENSE
```

---

## 📝 Licença
Este projeto está sob licença **MIT** — use, compartilhe e adapte. ✨
