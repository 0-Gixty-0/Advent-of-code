package Day2;

public class Main {

    public static void main(String[] args) {
        // System.out.println(ReadFromFile.getFileContents("Day2/testinput.txt"));
        System.out.println(CalculateScore.calculate(ReadFromFile.getFileContents("Day2/input.txt")));
        System.out.println(CalculateScore.calculatePart2(ReadFromFile.getFileContents("Day2/input.txt")));
        System.out.println(CalculateScoreImproved.calculatePart2(ReadFromFile.getFileContents("Day2/input.txt")));
    }
}
