#  define INT_MIN   (-INT_MAX - 1)
#  define INT_MAX   2147483647

int reverse(int x){
    long ret = 0;
    
      
    while(x!=0)
    {
        ret = ret*10 + (x%10);
        x = x/10;
        if( (ret < INT_MIN) || (ret > INT_MAX))
        {
            ret = 0;
            break;
        }
    }
    ret = (int)ret;
    return ret;
 
}


