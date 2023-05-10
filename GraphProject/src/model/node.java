
package model;

import java.util.ArrayList;

public class node {
    private String text;
    private double textPoint;
    private double anlamBenzerligi;
    private int tresholduGecenCumleSayisi;
    private ArrayList<node> texts;

    public node(String text, double textPoint, double anlamBenzerligi, int tresholduGecenCumleSayisi, ArrayList<node> texts) {
        this.text = text;
        this.textPoint = textPoint;
        this.anlamBenzerligi = anlamBenzerligi;
        this.tresholduGecenCumleSayisi = tresholduGecenCumleSayisi;
        this.texts = texts;
    }

    public node() {
    }
    
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public double getCumlePuani() {
        return textPoint;
    }

    public void setCumlePuani(double textPoint) {
        this.textPoint = textPoint;
    }

    public double getAnlamBenzerligi() {
        return anlamBenzerligi;
    }

    public void setAnlamBenzerligi(double anlamBenzerligi) {
        this.anlamBenzerligi = anlamBenzerligi;
    }

    public int getSiniriGecenCumleSayisi() {
        return tresholduGecenCumleSayisi;
    }

    public void setSiniriGecenCumleSayisi(int tresholduGecenCumleSayisi) {
        this.tresholduGecenCumleSayisi = tresholduGecenCumleSayisi;
    }

    public ArrayList<node> getTexts() {
        return texts;
    }

    public void setTexts(ArrayList<node> texts) {
        this.texts = texts;
    }
    
    
    
    
}
