package com.sockets.rpc;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import org.json.JSONObject;
import java.util.HashMap;

public class ClientStub {
    private Socket socket;
    private OutputStreamWriter outObj;
    private PrintWriter out;
    private BufferedReader buf;
    private HashMap<String, HashMap<String, String[]>> methodList;

    public ClientStub(String ipAddress, int port) throws Exception {
        socket = new Socket(ipAddress, port);
        outObj = new OutputStreamWriter(socket.getOutputStream());
        out = new PrintWriter(outObj);
        buf = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }

    public void getMethods() throws Exception {
        out.println("BROADCAST");
        outObj.flush();
        String response = buf.readLine();
        System.out.println(response);
        // JSONObject json = new JSONObject(response);
        // System.out.println(json.keySet());
    }

    // public static void main(String[] args) throws Exception {
	   //  //Enter ip address of server here 
	   //  String ipAddress = "localhost";
	   //  //Enter port number on which client will be listening here
	   //  int port = 1234;
	   //  Socket soc = new Socket(ipAddress, port);

	   //  String message = "Hello Server";
    //     JSONObject obj = new JSONObject();
    //     obj.put("message", message);

    //     OutputStreamWriter outObj = new OutputStreamWriter(soc.getOutputStream());
    //     // outObj.write(obj.toString());
    //     PrintWriter out = new PrintWriter(outObj);
    //     // out.println(obj.toString());
    //     out.println("BROADCAST");
    //     outObj.flush();

    //     BufferedReader br = new BufferedReader(new InputStreamReader(soc.getInputStream()));
    //     String response = br.readLine();
    //     System.out.println("Server's response is : " + response);
    // }
}
