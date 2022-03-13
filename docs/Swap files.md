## Criação de "swap files"

"Swap" é um espaço de disco usado para a expansão da memória RAM, utilizando a troca de páginas, que são copiadas da RAM para esse espaço, quando esta fica cheia.

Quando o sistema Linux fica sem RAM disponível, as páginas inativas são copiadas da RAM para esse espaço de troca.

Os comandos aqui apresentados foram testados no ubuntu 18.04, mas deverão funcionar noutros sistemas Linux.

### Verificação do espaço de swap existente
Para verificar o espaço de swap existente deve-se executar o comando:

    sudo swapon --show
  
Se não houver output, o sistema não tem espaço de troca habilitado.

Caso contrário, deverá surgir um output semelhante ao seguinte:

    NAME      TYPE      SIZE USED PRIO
    /dev/sda2 partition 1.9G   0B   -2

### Criação da "swap file"
Neste exemplo, adicionaremos o espaço de 1G. Para adicionar um espaço diferente, basta substituir 1G pelo tamanho do espaço que se pretender.

- 1 - Começa-se por criar o ficheiro que será utilizado:

        sudo fallocate -l 1G /swapfile

Se o _fallocate_ não estiver instalado ou se surgir uma mensagem de erro a informar que o _fallocate_ falhou, utilizar o seguinte comando para criar o ficheiro:

        sudo dd if=/dev/zero of=/swapfile bs=1024 count=1048576

- 2 - Apenas o root deve ser capaz de escrever e ler o ficheiro de troca. Definem-se as permissões corretas com o comando:
  
        sudo chmod 0600 /swapfile

- 3 - Utilizar o utilitário _mkswap_ para configurar o ficheiro como área de troca do Linux com o comando:
  
        sudo mkswap /swapfile

- 4 - Ativar a "swap file" utilizado:
  
        sudo swapon /swapfile
  
  Para tornar a alteração permanente altera-se o ficheiro "/etc/fstab" com o comando:
    
        sudo nano /etc/fstab
  
  colocando lá a linha:
    
        /swapfile swap swap defaults 0 0
  
- 5 - Verificar que a "swap file" está ativa utilizado os comandos _swapon_ e _free_ como exemplificado a seguir:
  
        sudo swapon --show
        
        Resultado:
        NAME      TYPE  SIZE   USED PRIO
        /swapfile file 1024M 507.4M   -1

    
        sudo free -h
        
        Resultado:
                    total        used        free      shared  buff/cache   available
        Mem:           488M        158M         83M        2.3M        246M        217M
        Swap:          1.0G        506M        517M

### Remoção da "swap file"
Para desativar e remover a "swap file", seguir as seguintes etapas:

- 1 - Começa-se por desativar o ficheiro usado com o colmando:
  
        sudo swapoff -v /swapfile

- 2 - De seguida remover a linha _/swapfile swap swap defaults 0 0_ do ficheiro _"/etc/fstab"_.

- 3 - Finalmente remover o ficheiro do sistema usado com o colmando:
  
        sudo rm /swapfile





