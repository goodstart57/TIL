# 소수 판별 함수(에라토스테네스의 체)
def get_prime_dict(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    prime_dict = {i:True for i in range(n+1)} # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
    prime_dict[0] = False
    prime_dict[1] = False
    
    # 에라토스테네스의 체
    for i in range(2, int(sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if prime_dict[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                prime_dict[i * j] = False
                j += 1
                
    return prime_dict