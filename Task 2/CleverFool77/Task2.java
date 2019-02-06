/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication7;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author lekhika
 */
public class JavaApplication7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       String email = "something@gmail.com";
       String password = "hhhhhhhh";
        String regex = "^(.+)@gmail(\\.)(com)$";
        String regex1 = "^.{8,}$";

        Pattern pattern = Pattern.compile(regex);
            Matcher matcher = pattern.matcher(email);
            System.out.println(email + " : " + matcher.matches());
        Pattern pattern1 = Pattern.compile(regex1);
        Matcher matcher1 = pattern1.matcher(password);
            System.out.println(password + " : " + matcher1.matches());

    }
}
