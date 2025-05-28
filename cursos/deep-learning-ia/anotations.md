# ChatGPT Prompt Engineering for Developers

## Aula 01

- O poder real dos LLM está em usar as APIs para desenvolver aplicações
- Existem dois tipos de LLM: Base LLM e Instruction Tuned LLM
- **Base LLM** →prevêm a próxima palavra, baseado on treinamento de texto com dados
- **Instruction Tuned LLM →** tenta seguir instruções.  Ajuste fino nas instruções e boas tentativas de segui-las
    - Esses modelos são feitos da seguinte forma:
    1.  Pega-se um **Base LLM com uma enorme quantidade de dados** em forma de texto (text data) 
    2. São treinados com o ajuste fino (fine tune) com inputs e outputs que são instruções e como seguir essas instruções 
    3. São refinados com RLHF (Reinforcement Learning with Human Feedbback)
- Na utilização do modelo, pense que você está dando uma tarefa parefa alguém inteligente, mas que não conhece as especificidades da sua tarefa. Então, quando o modelo não funciona, às vezes é porque as instruções não foram claras suficientes
- Pense como se fosse passar essa tarefa para outra pessoa, as instruções precisam ser detalhadas → instruções claras e específicas

## Aula 02

### Principle 1 → write clear and specific instructions

- Tactic 1: use delimiters
    - Triple quote: “””
    - Triple backticks: ```
    - Triple dashes: - - -
    - Angle brackets: <>
    - XML tags: <tag> </tag>
- Para evitar injeção de código, utilize os delimitadores
- Tactic 2: ask for a structured output
    - HTML, JSON
- Tactic 3: check wether conditions are satisfied
    - Check assumptions required to do the task
- Tactic 4: Few shot prompting
    - Give sucessful examples of completing tasks
    - Then ask model to perform the task

### Principle 2 → give the model time to think

- É como dar a alguém um complicada de matemática para fazer em um curto período de tempo → mesmo que a pessoa for boa, o resultado vai sair com pressa
- Instruct the model to thin more about a problem
- Tactic 1: specify the steps to complete a task
    - Step 1: …
    - Step 2: …
    - Step N: …
- Tactic 2: instruct the model to work out its own solution before rushing to a conclusion

### Model Limitations

- Hallucination
- Makes statements that sound plausible but are not true
- Reducing hallucinations
    - Ask the model to: first find relevant information, then answer the question based on the relevant information

## Aula 03

- Iterative prompt development: idea → implementation (code/data) → experiment result → error Analysis
- **Prompt guidelines**
    - Be clear and specific
    - Analyze why results does not give desired output
    - Refine the idea and the prompt
    - Repeat
- It’s a process developing good prompts → é imprescindível fazer a análise de erros e ir refinando os prompts
- Os modelos não são ótimos em seguir instruções sobre o tamanho do texto. Se pedir um texto de 50 palavras, por exemplo, ele pode te retornar 52, 51..
- As boas práticas mais importantes são **ser claro e específico →** escreva um prompt, veja o resultado e a partir disso você vai refinando
- Lembre-se que você pode escolher o formato que o outuput vai sair (.txt, HTML, JSON, etc)

### **Iterative Process**

- Try something
- Analyze where the result does not give what you want
- Clarify instructions, give more time to think
- Refine prompts whit a batch of examples
