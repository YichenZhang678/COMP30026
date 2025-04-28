#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TOTAL_NUMBERS 821
#define SAMPLE_SIZE 25

int main() {
    int numbers[TOTAL_NUMBERS];
    int selected[SAMPLE_SIZE];
    int i, j, index;
    int is_duplicate;

    // 初始化随机数种子
    srand(time(NULL));

    // 假设数组从1到2713初始化
    for (i = 0; i < TOTAL_NUMBERS; i++) {
        numbers[i] = i + 1;
    }

    // 抽取20个随机数
    for (i = 0; i < SAMPLE_SIZE; i++) {
        do {
            is_duplicate = 0;
            index = rand() % TOTAL_NUMBERS;  // 生成随机索引

            // 检查是否有重复
            for (j = 0; j < i; j++) {
                if (selected[j] == numbers[index]) {
                    is_duplicate = 1;
                    break;
                }
            }
        } while (is_duplicate);  // 如果重复则重新生成

        selected[i] = numbers[index];  // 保存选中的数字
    }

    // 打印抽取的20个数字
    printf("随机抽取的20个数字是:\n");
    for (i = 0; i < SAMPLE_SIZE; i++) {
        printf("%d ", selected[i]);
    }

    return 0;
}
