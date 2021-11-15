package com.sockets.rpc;

import java.util.HashMap;

public class Client {
	public static void main(String[] args) throws Exception {
		System.out.println(args[0]);
		ClientStub stub = new ClientStub(args[0], 5000);
		// HashMap methodList = stub.getMethods();
		stub.getMethods();
		// stub.call("<function>", <params>);
	}
}