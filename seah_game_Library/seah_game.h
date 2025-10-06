#ifndef SEAH_GAME_H
#define SEAH_GAME_H


typedef enum {
    UR_PLUS,
    UR,
    SSR_PLUS,
    SSR,
    SR_PLUS,
    SR,
    R_PLUS,
    R,
    RARITY_COUNT
} Rarity;


typedef struct {
    Rarity rarity;
    int attempts;
    int crystals_used;
} GachaResult;


GachaResult pull_once();


void pull_11_times();


double expected_attempts_for(Rarity target, int simulations);


GachaResult pull_until(Rarity target);

#endif
