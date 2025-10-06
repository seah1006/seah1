#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "seah_game.h"

int main() {
    srand(time(NULL));

   
    GachaResult one = pull_once();
    printf("🎯 1회 뽑기 결과: %s (크리스탈 %d)\n",
           (one.rarity >= 0 && one.rarity < RARITY_COUNT) ? 
           (const char*[]){ "UR+", "UR", "SSR+", "SSR", "SR+", "SR", "R+", "R" }[one.rarity] : "알 수 없음",
           one.crystals_used);

    
    pull_11_times();

   
    double avg = expected_attempts_for(SSR, 100000);
    printf("📊 SSR 이상 뽑기까지 평균 시도 횟수: %.2f회 (%.0f 크리스탈)\n", avg, avg * 200);

    
    GachaResult pity = pull_until(SSR_PLUS);
    printf("🎉 SSR+ 이상 획득까지 %d회 시도 (%d 크리스탈)\n",
           pity.attempts, pity.crystals_used);

    return 0;
}
