#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "seah_game.h"

// 등급별 확률 테이블 (누적 확률)
static const double rarity_prob[RARITY_COUNT] = {
    0.001,   // UR+ 0.1%
    0.005,   // UR  0.4%
    0.015,   // SSR+ 1.0%
    0.045,   // SSR  3.0%
    0.110,   // SR+  6.5%
    0.230,   // SR  12.0%
    0.500,   // R+  27.0%
    1.000    // R   50.0%
};


static const char *rarity_names[RARITY_COUNT] = {
    "UR+","UR","SSR+","SSR","SR+","SR","R+","R"
};


GachaResult pull_once() {
    double r = (double)rand() / RAND_MAX;
    GachaResult result;
    result.attempts = 1;
    result.crystals_used = 200;

    for (int i = 0; i < RARITY_COUNT; i++) {
        if (r < rarity_prob[i]) {
            result.rarity = i;
            return result;
        }
    }
    result.rarity = R;
    return result;
}


void pull_11_times() {
    printf("🔮 11회 연속 뽑기 결과:\n");
    for (int i = 0; i < 11; i++) {
        GachaResult r = pull_once();
        printf("[%2d회] 등급: %s\n", i + 1, rarity_names[r.rarity]);
    }
    printf("💎 사용한 크리스탈: 2000\n\n");
}


double expected_attempts_for(Rarity target, int simulations) {
    long long total_attempts = 0;

    for (int i = 0; i < simulations; i++) {
        int attempts = 0;
        while (1) {
            attempts++;
            GachaResult r = pull_once();
            if (r.rarity <= target || attempts >= 200) break; // 천장 적용
        }
        total_attempts += attempts;
    }

    return (double)total_attempts / simulations;
}

// 특정 등급 이상이 나올 때까지 뽑기 (천장 시스템 포함)
GachaResult pull_until(Rarity target) {
    GachaResult result;
    result.attempts = 0;
    result.crystals_used = 0;

    while (1) {
        result.attempts++;
        result.crystals_used += 200;
        GachaResult current = pull_once();
        if (current.rarity <= target || result.attempts >= 200) {
            result.rarity = current.rarity;
            break;
        }
    }

    return result;
}
