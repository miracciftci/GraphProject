
package business;

import java.util.ArrayList;

public class NodeManager {
    
    
    // cumlenin kelimelere ayrismasi
    public ArrayList<String> Tokenization(String text){
        ArrayList<String> words = new ArrayList<>();
        
        String[] array = text.split(" ");
   
        for(String str : array){
            if(!str.trim().equals(""))
                words.add(str.trim());
        }
        
        return words;
    }
    
    
    // gereksiz kucuk soz obeklerinin kaldirilmasi
    public ArrayList<String> StopWord(ArrayList<String> words){
        ArrayList<String> wordsArray = new ArrayList<>();
        
        for(String str : words){
            if(str.equals("and") || str.equals("or") ||str.equals("but") ||str.equals("a") ||str.equals("the") ||str.equals("if") ||str.equals("on")||
                    str.equals("an") || str.equals("for") ||str.equals("with") ||str.equals("am") ||str.equals("is") ||str.equals("are") ||str.equals("at") ||str.equals("in")){
                continue;
            }
            
            wordsArray.add(str);
        }
        return wordsArray;
    }
    
    // noktalama isaretlerinin kaldirilmasi
    public String Punctuation(String text){
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("\"", "").
                replace("'", "").replace("(", "").replace(")", "").replace(";", "").
                replace(":", "").replace("\\", "").replace("-", "").replace("\"", "").
                replace("!", "").replace("{", "").replace("}", "").replace("<", "").replace(">", "");
        return text;
    }
    
    // kelimelerin kokunun bulunmasi
    public String Stemming(String text){
   
        return text;
    }
}
