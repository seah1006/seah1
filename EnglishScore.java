package test;

public class EnglishScore implements Comparable<EnglishScore> {
    String name;
    int score;

    public EnglishScore(String name, int score) {
        this.name = name;
        this.score = score;
    }

    @Override
    public String toString() {
        return name + ", " + score;
    }

    @Override
    public int compareTo(EnglishScore e) {
        return this.score - e.score;
    }
}
