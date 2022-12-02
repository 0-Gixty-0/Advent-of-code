package Day2;

import java.util.ArrayList;

public class CalculateScore {
    enum GameStatus {
        WIN,
        LOSS,
        DRAW
    }

    enum Selection {
        ROCK,
        PAPER,
        SCISSORS
    }


    public static int calculate(ArrayList<String> data) {
        int totalScore = 0;
        for (String round : data) {
            String[] roundArr = round.split(" ");
            GameStatus roundStatus = determineRoundStatus(roundArr[0], roundArr[1]);
            totalScore += determineRoundScore(roundStatus);
            totalScore += determineThrowScore(roundArr[1]);
            
        }
        return totalScore;
    }

    public static int calculatePart2(ArrayList<String> data) {
        int totalScore = 0;
        for (String round : data) {
            String[] roundArr = round.split(" ");
            Selection mySelection = determineSelection(roundArr[0], roundArr[1]);
            totalScore += getRoundScore(roundArr[1]);
            totalScore += getThrowScore(mySelection);
            
        }
        return totalScore;
    }

    private static int getThrowScore(Selection mySelection) {
        switch (mySelection) {
            case ROCK: 
                return 1;
            case PAPER: 
                return 2;
            case SCISSORS:
                return 3;
            default:
                return 0;
        }
    }

    private static int getRoundScore(String string) {
        switch (string) {
            case "X":
                return 0;
            case "Y":
                return 3;
            case "Z":
                return 6;
        }
        return 0;
    }

    private static Selection determineSelection(String op, String me) {
        switch (op) {
            case "A":
                return getSelectionWhenRock(me);
            case "B":
                return getSelectionWhenPaper(me);
            case "C":
                return getSelectionWhenScissors(me);
        }
        return null;
    }

    private static Selection getSelectionWhenScissors(String me) {
        switch (me) {
            case "X":
                return Selection.PAPER;
            case "Y":
                return Selection.SCISSORS;
            case "Z":
                return Selection.ROCK;
        }
        return null;
    }

    private static Selection getSelectionWhenPaper(String me) {
        switch (me) {
            case "X":
                return Selection.ROCK;
            case "Y":
                return Selection.PAPER;
            case "Z":
                return Selection.SCISSORS;
        }
        return null;
    }

    private static Selection getSelectionWhenRock(String me) {
        switch (me) {
            case "X":
                return Selection.SCISSORS;
            case "Y":
                return Selection.ROCK;
            case "Z":
                return Selection.PAPER;
        }
        return null;
    }

    private static int determineRoundScore(GameStatus roundStatus) {
        switch (roundStatus) {
            case WIN: {
                return 6;
            }
            case DRAW: {
                return 3;
            }
            default:
                return 0;
        }
    }

    private static int determineThrowScore(String symbol) {
        switch (symbol) {
            case "X":
                return 1;
            case "Y":
                return 2;
            case "Z":
                return 3;
            default:
                return 0;
        }
    }

    private static GameStatus determineRoundStatus(String op, String me) {
        switch (op) {
            case "A":
                return getGameStatusWhenRock(me);
            case "B":
                return getGameStatusWhenPaper(me);
            case "C":
                return getGameStatusWhenScissors(me);
            }
        return null;
    }

    private static GameStatus getGameStatusWhenScissors(String me) {
        switch (me) {
            case "X":
                return GameStatus.WIN;
            case "Y":
                return GameStatus.LOSS;
            case "Z":
                return GameStatus.DRAW;
        }
        return null;
    }

    private static GameStatus getGameStatusWhenPaper(String me) {
        switch (me) {
            case "X":
                return GameStatus.LOSS;
            case "Y":
                return GameStatus.DRAW;
            case "Z":
                return GameStatus.WIN;
        }
        return null;
    }

    private static GameStatus getGameStatusWhenRock(String me) {
        switch (me) {
            case "X":
                return GameStatus.DRAW;
            case "Y":
                return GameStatus.WIN;
            case "Z":
                return GameStatus.LOSS;
        }
        return null;
    }
}
