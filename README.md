# A Simple CRUD API

Uma simples API que permite o usuário criar, ler, atualizar e deletar um usuário, além de manter essas informações salvas em um banco de dados.

### **Instalando o ambiente virtual**
A instalação de uma virtualenv é feita utilizando o pip, gerenciador de pacotes do Python. Após instalar o pip, utilizamos o comando abaixo para instalar o pacote virtualenv em nosso computador:

```
pip install virtualenv
```

Feito isso, o pacote estará instalado e pronto para ser utilizado. Agora já podemos criar e gerenciar nossos ambientes virtuais.

### **Criando o ambiente virtual**

Será necessário criar um ambiente virtual. Nesse caso, iremos utilizar a biblioteca virtualenv.
O processo de criação de uma virtualenv é bastante simples e pode ser feito utilizando um único comando, como podemos ver abaixo:

```
powershell
virtualenv venv
```

```
bash
virtualenv venv
```

O mais comum é criar a virtualenv na raiz do projeto que ela irá pertencer. Isso permite uma organização maior das virtualenvs que possuímos em nosso computador:
Com isso, criamos a virtualenv do projeto chamada “venv”. É ela quem vai comportar todos os pacotes necessários para a execução do projeto.

### **Ativando o ambiente virtual**

Após criar uma virtualenv, precisamos ativá-la para que possamos instalar os pacotes necessários do projeto. Para isso, utilizamos o seguinte comando:

```
powershell
nome_da_virtualenv/Scripts/Activate.ps1
```

```
bash
source nome_da_virtualenv/bin/activate (Linux ou macOS)
```

O comando acima irá ativar a virutalenv:
Note que o nome da virtualenv, agora, é exibido antes do caminho do diretório em que estamos. Isso indica que a virtualenv foi ativada com sucesso.

***Observação***

Caso o processo de ativação retorne erro, executar o seguinte comando:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

### **Instalando as depedências**

Dentro do ambiente virtual, basta digitar o comando:

```
pip install -r requirements.txt
```

### **Ativando a API**
```
python app.py
```
