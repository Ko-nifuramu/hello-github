import java.util.Arrays;

class Recursion-problem-black-jack.java{
    public static boolean winnerBlackjack(String[] playerCards, String[] houseCards){
        int playerPoint=0;
        int dealerPoint=0;

        for(int i=0; i<playerCards.length; i++){
            playerPoint += cardPoint(playerCards[i]);
        }

        //System.out.println(playerPoint);

        for(int i=0; i<houseCards.length; i++){
            dealerPoint += cardPoint(houseCards[i]);
        }

        //System.out.println(dealerPoint);

        if(playerPoint < 0 || dealerPoint < 0){
            System.out.println("Attention : There may be inapproapriate cards !!");
            return false;
        }
        else if(playerPoint > 21) return false;
        else if(playerPoint == dealerPoint) return false;
        else if(dealerPoint > 21) return true;
        else if(playerPoint > dealerPoint) return true;
        else return false;
    }

    public static int cardPoint(String card){
        if(card.length() == 2){
            char[] c = card.toCharArray();
            return outputPoint(c[1]);
        }
        //10だけは3文字ある
        else if(card.length() == 3){
            return 10;
        }
        else return -100;//トランプのカードではないものが入力された場合
    }

    public static int outputPoint(char number){
        if((int)number == (int)'A') return 1;
        else if((int)number == (int)'J') return 11;
        else if((int)number == (int)'Q') return 12;
        else if((int)number == (int)'K') return 13;
        else return Character.getNumericValue(number); 
    }
   public static void main(String[] args){
        winnerBlackjack(["♣4","♥7","♥7"],["♠Q","♣J"])//->true
        return 0;
   }
}
