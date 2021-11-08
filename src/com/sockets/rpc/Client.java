package com.sockets.rpc;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
    public static void main(String[] args) throws Exception {
	    String ipAddress = "192.168.1.2";
	    int port = 5000;
	    Socket soc = new Socket(ipAddress, port);

	    String request = "Hello Server";

        OutputStreamWriter outObj = new OutputStreamWriter(soc.getOutputStream());
        PrintWriter out = new PrintWriter(outObj);
        out.println(request);
        outObj.flush();

        BufferedReader br = new BufferedReader(new InputStreamReader(soc.getInputStream()));
        String response = br.readLine();
        System.out.println("Server's response is : " + response);
    }
}
