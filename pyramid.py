'''
$
$$
$$$
$$$$
$$$$$
$$$$$$
$$$$$$$
$$$$$$$$
$$$$$$$$$
$$$$$$$$$$
'''
def pyramid_left_to_right(number):
    for i in range(number):
        print(f"{(i+1)*'$'}")

'''
         $
        $$
       $$$
      $$$$
     $$$$$
    $$$$$$
   $$$$$$$
  $$$$$$$$
 $$$$$$$$$
$$$$$$$$$$
'''
def pyramid_right_to_left(number):
    for i in reversed(range(number)):
        print(f"{i*' ' + '$'*(number-i)}")


'''
         $         
        $$$        
       $$$$$       
      $$$$$$$      
     $$$$$$$$$     
    $$$$$$$$$$$    
   $$$$$$$$$$$$$   
  $$$$$$$$$$$$$$$  
 $$$$$$$$$$$$$$$$$ 
$$$$$$$$$$$$$$$$$$$
'''
def pyramid_mid(number):
    for i in reversed(range(number)):
        left_dollars = ' ' * i + '$' * (number - i - 1)
        print(left_dollars + '$' + left_dollars[::-1])


def main():
    pyramid_left_to_right(10)
    pyramid_right_to_left(10)
    pyramid_mid(10)


if __name__ == "__main__":
    main()