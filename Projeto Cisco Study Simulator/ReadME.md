English

Cisco Study Simulator

Interactive Cisco command simulator developed for educational purposes. The project started as a personal study tool to gain a practical understanding of the basic operation of a Cisco switch. The initial idea was to test commands, observe their effects, and validate concepts learned while studying computer networks. Over time, the project evolved to simulate different CLI modes, VLANs, interfaces, Port Security, connectivity, and configuration persistence.

About the Project

Cisco Study Simulator is a web application that reproduces, in a simplified manner, some of the concepts found in Cisco switch configuration. The goal is not to replace tools such as Cisco Packet Tracer or real networking equipment, but to provide a simple environment for practicing commands and understanding the logic behind network configurations.
The project also includes a guided objectives system, allowing users to study specific concepts by following a sequence of commands.

Features

Interactive CLI similar to the interface of a Cisco switch

User EXEC and Privileged EXEC modes

Global configuration mode

Hostname configuration

Console and VTY password configuration

Enable secret configuration

Custom VLANs

Access port configuration

Trunk port configuration

VLAN 1 interface

IP address configuration

Connectivity testing with ping

Port Security

Sticky MAC Address

Security violation simulation

Simulated MAC address table

Interface status

RAM and NVRAM simulation

show commands

Command history

Contextual help system

Guided study objectives

Command Tree for viewing the CLI hierarchy

Simulated switch reset

Examples
Entering Privileged EXEC Mode
Switch> enable
Switch#

Configuring a VLAN
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name Vendas

Configuring an Access Port
Switch(config)# interface fastethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10

Configuring Port Security
Switch(config)# interface fastethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security mac-address sticky

Saving the Configuration
Switch# copy running-config startup-config


The following commands are also supported:

Switch# write memory


or:

Switch# wr

Verification Commands

Some of the available commands include:

show running-config
show vlan brief
show mac address-table
show interfaces status
show ip interface brief


These commands display information about the current state of the simulated switch.

Study Objectives

The simulator includes several guided exercises.

1. Configure a Management IP Address

Practice:

interface vlan 1
ip address
no shutdown
ping

2. Configure Access Passwords

Practice:

enable secret
line console 0
line vty 0 15
password
login
service password-encryption

3. Create VLANs and Configure Ports

Practice:

vlan
name
interface fastethernet
switchport mode access
switchport access vlan
switchport mode trunk

4. Port Security

Practice:

switchport port-security
switchport port-security mac-address sticky


It is also possible to simulate a security violation:

atacar fa0/1

RAM and NVRAM

The simulator provides a simplified representation of the difference between the current configuration and the saved configuration.

The running configuration represents running-config.

The saved configuration represents startup-config.

To save the configuration:

copy running-config startup-config


To erase the saved configuration:

erase startup-config


The following command:

reload


simulates a switch reboot and allows users to observe the behavior of the saved configuration.

Technologies

The project was developed using native web technologies:

HTML5

CSS3

JavaScript

The current version does not depend on external frameworks or libraries.

How to Run

Since this is a static web application, simply open the index.html file in a modern web browser.

You can also use tools such as Live Server during development.

Current Structure

The first version of the project was developed entirely within a single HTML file.

Cisco-Study-Simulator/
│
├── index.html
└── README.md


This structure was sufficient during the initial phase, when the project was simply a personal study tool.

As the simulator grows, separating the HTML, CSS, and JavaScript files may make the code easier to maintain and expand.

Limitations

The project is an educational simulation and does not implement real Cisco IOS.

Some behaviors are simplified, including:

VLAN operation

Port Security

Trunking

ping

MAC addresses

RAM and NVRAM

Interface states

For example, ping does not use real ICMP. The response is determined by the simulator's internal logic.

Project Background

The project started as a simple tool, initially focused on connectivity testing and basic commands.

As new topics were studied, additional features were gradually added:

Ping
  ↓
CLI
  ↓
Switch Modes
  ↓
Configuration
  ↓
VLANs
  ↓
Interfaces
  ↓
Port Security
  ↓
RAM / NVRAM
  ↓
Guided Objectives


The project continues to be developed as part of the learning process in computer networking.

Status

In development.

New features and improvements will be added as new networking and Cisco concepts are studied.

License

The project license has not yet been defined.


===============================================
===============================================


Português Brasileiro

Cisco Study Simulator

Simulador interativo de comandos Cisco desenvolvido para fins educacionais. O projeto começou como uma ferramenta pessoal de estudo para entender, na prática, o funcionamento básico de um switch Cisco. A ideia inicial era testar comandos, observar seus efeitos e validar conceitos aprendidos durante os estudos de redes. Com o tempo, o projeto evoluiu e passou a simular diferentes modos da CLI, VLANs, interfaces, Port Security, conectividade e persistência de configurações.

Sobre o projeto

O Cisco Study Simulator é uma aplicação web que reproduz de forma simplificada alguns conceitos encontrados na configuração de switches Cisco. O objetivo não é substituir ferramentas como Cisco Packet Tracer ou equipamentos reais, mas oferecer um ambiente simples para praticar comandos e entender a lógica por trás das configurações. O projeto também possui um sistema de objetivos guiados, permitindo estudar determinados conceitos seguindo uma sequência de comandos.

Funcionalidades

CLI interativa semelhante à interface de um switch Cisco

Modos User EXEC e Privileged EXEC

Modo de configuração global

Configuração de hostname

Configuração de senhas de Console e VTY

Configuração de enable secret

VLANs personalizadas

Configuração de portas Access

Configuração de portas Trunk

Interface VLAN 1

Configuração de endereço IP

Teste de conectividade com ping

Port Security

MAC Address Sticky

Simulação de violação de segurança

Tabela MAC simulada

Status das interfaces

Simulação de RAM e NVRAM

Comandos show

Histórico de comandos

Sistema de ajuda contextual

Objetivos de estudo guiados

Command Tree para visualizar a hierarquia da CLI

Reset do switch simulado

Exemplos
Entrando no modo privilegiado
Switch> enable
Switch#

Configurando uma VLAN
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name Vendas

Configurando uma porta Access
Switch(config)# interface fastethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10

Configurando Port Security
Switch(config)# interface fastethernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security mac-address sticky

Salvando a configuração
Switch# copy running-config startup-config


Também são aceitos:

Switch# write memory


ou:

Switch# wr

Comandos de verificação

Alguns dos comandos disponíveis são:

show running-config
show vlan brief
show mac address-table
show interfaces status
show ip interface brief


Esses comandos apresentam informações sobre o estado atual do switch simulado.

Objetivos de estudo

O simulador possui alguns exercícios guiados:

1. Configurar IP de gerenciamento

Prática de:

interface vlan 1
ip address
no shutdown
ping

2. Configurar senhas de acesso

Prática de:

enable secret
line console 0
line vty 0 15
password
login
service password-encryption

3. Criar VLANs e configurar portas

Prática de:

vlan
name
interface fastethernet
switchport mode access
switchport access vlan
switchport mode trunk

4. Port Security

Prática de:

switchport port-security
switchport port-security mac-address sticky


Também é possível simular uma violação:

atacar fa0/1

RAM e NVRAM

O simulador representa de forma simplificada a diferença entre a configuração atual e a configuração salva.

A configuração em execução representa a running-config.

A configuração salva representa a startup-config.

Para salvar:

copy running-config startup-config


Para apagar a configuração salva:

erase startup-config


O comando:

reload


simula a reinicialização do switch e permite observar o comportamento da configuração salva.

Tecnologias

O projeto foi desenvolvido utilizando tecnologias web nativas:

HTML5

CSS3

JavaScript

A versão atual não depende de frameworks ou bibliotecas externas.

Como executar

Por ser uma aplicação web estática, basta abrir o arquivo index.html em um navegador moderno.

Também é possível utilizar ferramentas como Live Server durante o desenvolvimento.

Estrutura atual

A primeira versão do projeto foi desenvolvida inteiramente em um único arquivo HTML.

Cisco-Study-Simulator/
│
├── index.html
└── README.md


Essa estrutura foi suficiente durante a fase inicial, quando o projeto era apenas uma ferramenta pessoal de estudos.

Com o crescimento do simulador, uma futura separação entre HTML, CSS e JavaScript pode facilitar a manutenção e expansão do código.

Limitações

O projeto é uma simulação educacional e não implementa o Cisco IOS real.

Alguns comportamentos são simplificados, incluindo:

Funcionamento das VLANs

Port Security

Trunk

ping

Endereços MAC

RAM e NVRAM

Estados das interfaces

O ping, por exemplo, não utiliza ICMP real. A resposta é determinada pela lógica interna do simulador.

Origem do projeto

O projeto começou de forma simples, inicialmente com testes de conectividade e comandos básicos.

Conforme novos conteúdos eram estudados, novas funcionalidades foram sendo adicionadas:

Ping
  ↓
CLI
  ↓
Modos do switch
  ↓
Configuração
  ↓
VLANs
  ↓
Interfaces
  ↓
Port Security
  ↓
RAM / NVRAM
  ↓
Objetivos guiados


O projeto continua sendo desenvolvido como parte do processo de aprendizado em redes de computadores.

Status

Em desenvolvimento.

Novas funcionalidades e melhorias serão adicionadas conforme novos conceitos de redes e Cisco forem estudados.

Licença

A licença do projeto ainda deve ser definida.
