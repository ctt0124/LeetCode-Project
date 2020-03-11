

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i,j;
    int temp = 0;
    int* ret = (int*) malloc(2*sizeof(int));
    
    if(ret!=NULL && returnSize != NULL && numsSize!=0)
    {

        for(i = 0;i<numsSize;i++)
        {
            
            temp = target - nums[i];

            for(j = i+1;j<numsSize;j++)
            {
                if(temp == nums[j])
                {
                    printf("j%d\n",j);
                    ret[0] = i;
                    ret[1] = j;
                    *returnSize = 2;
                    break;
                }
            }
            
           
        }

        return ret;
    }
    else{
        return 0;
    }
    
}
