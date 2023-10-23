package br.com.dsm.stickers;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableAutoConfiguration
public class StickersApplication {

	public static void main(String[] args) {
		SpringApplication.run(StickersApplication.class, args);
	}
}
