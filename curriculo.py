from flask import Flask

app = Flask(__name__)


@app.route("/")
def aula():
    return
'''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Estudante de TI</title>

</head>
<body>

    <header>
        <h1>[Seu Nome Completo]</h1>
        <div class="header-info">
            [Seu Bairro], [Sua Cidade] - [Seu Estado] <br>
            [Seu Telefone] | [Seu Email] <br>
            <a href="[Link do seu LinkedIn]" target="_blank">LinkedIn</a> | 
            <a href="[Link do seu GitHub]" target="_blank">GitHub</a>
        </div>
    </header>

    <section>
        <h2>Resumo Profissional</h2>
        <p>Estudante de [Nome do Curso, ex: Análise e Desenvolvimento de Sistemas] apaixonado por tecnologia. Busco oportunidade como estagiário/júnior na área de TI, com foco em [Sua área de interesse, ex: Desenvolvimento Web/Data Science/Suporte]. Conhecimentos em lógica de programação, banco de dados e [Tecnologia principal, ex: Python/JavaScript].</p>
    </section>

    <section>
        <h2>Formação Acadêmica</h2>
        <div class="section">
            <span class="date">[Mês/Ano Início] – [Previsão Formatura]</span>
            <div class="job-title">[Nome da Instituição de Ensino]</div>
            <div>[Nome do Curso]</div>
        </div>
    </section>

    <section>
        <h2>Projetos de TI</h2>
        <div class="section">
            <div class="job-title">[Nome do Projeto 1, ex: Sistema de Cadastro]</div>
            <ul>
                <li>Desenvolvido utilizando: [Tecnologias, ex: Python, Flask, SQLite].</li>
                <li>Funcionalidades: CRUD completo, autenticação de usuários e interface responsiva.</li>
                <li><a href="[Link do GitHub do Projeto]" target="_blank">Ver projeto no GitHub</a></li>
            </ul>
        </div>
        <div class="section">
            <div class="job-title">[Nome do Projeto 2, ex: Analisador de Dados]</div>
            <ul>
                <li>Desenvolvido utilizando: [Tecnologias, ex: Python, Pandas, Matplotlib].</li>
                <li>Objetivo: Automatizar a leitura de arquivos CSV e gerar dashboards para insights.</li>
            </ul>
        </div>
    </section>

    <section>
        <h2>Habilidades Técnicas</h2>
        <ul>
            <li><strong>Linguagens:</strong> [Ex: Python, JavaScript, SQL, C#]</li>
            <li><strong>Frameworks/Bibliotecas:</strong> [Ex: React, Flask, Bootstrap]</li>
            <li><strong>Ferramentas/Bancos de Dados:</strong> [Ex: Git, Docker, MySQL, PostgreSQL]</li>
            <li><strong>Sistemas Operacionais:</strong> [Ex: Windows, Linux/Ubuntu]</li>
        </ul>
    </section>

    <section>
        <h2>Cursos e Certificações</h2>
        <ul>
            <li>[Nome da Certificação/Curso] - [Plataforma, ex: Udemy/Alura] ([Ano])</li>
            <li>[Nome da Certificação/Curso] - [Plataforma, ex: Udemy/Alura] ([Ano])</li>
        </ul>
    </section>

    <section>
        <h2>Idiomas</h2>
        <ul>
            <li><strong>Português:</strong> Nativo</li>
            <li><strong>Inglês:</strong> [Nível, ex: Técnico/Intermediário]</li>
        </ul>
    </section>

</body>
</html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
