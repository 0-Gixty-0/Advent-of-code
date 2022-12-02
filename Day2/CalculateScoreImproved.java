package Day2;

import java.util.ArrayList;

public class CalculateScoreImproved {
    public static int calculatePart2(ArrayList<String> data) {
        int totalScore = 0;
        for (String round : data) {
            String[] roundArr = round.split(" ");
            totalScore += determineScore(roundArr[0], roundArr[1]);
        }
        return totalScore;
    }

    private static int determineScore(String op, String me) {
        switch (op) {
            case "A":
                return getScoreWhenRock(me);
            case "B":
                return getScoreWhenPaper(me);
            case "C":
                return getScoreWhenScissors(me);
        }
        return 0;
    }

    private static int getScoreWhenScissors(String me) {
        switch (me) {
            case "X":
                return 2;
            case "Y":
                return 6;
            case "Z":
                return 7;
        }
        return 0;
    }

    private static int getScoreWhenPaper(String me) {
        switch (me) {
            case "X":
                return 1;
            case "Y":
                return 5;
            case "Z":
                return 9;
        }
        return 0;
    }

    private static int getScoreWhenRock(String me) {
        switch (me) {
            case "X":
                return 3;
            case "Y":
                return 4;
            case "Z":
                return 8;
        }
        return 0;
    }
}
