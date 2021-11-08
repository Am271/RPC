package com.sockets.rpc;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) throws Exception{
        ServerSocket server = new ServerSocket(5000);

        System.out.println("I am waiting................");
        Socket soc = server.accept();
        System.out.println("Connected to client");

        BufferedReader br = new BufferedReader(new InputStreamReader(soc.getInputStream()));
        String request = br.readLine();
        System.out.println("Client request: " + request);

        String response = "Happy Diwali";
        OutputStreamWriter outObj = new OutputStreamWriter(soc.getOutputStream());
        PrintWriter out = new PrintWriter(outObj);
        out.println(response);
        out.flush();

        System.out.println("One communication cycle successfully completed");
    }
}
