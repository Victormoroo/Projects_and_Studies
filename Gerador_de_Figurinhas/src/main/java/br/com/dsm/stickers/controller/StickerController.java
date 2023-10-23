package br.com.dsm.stickers.controller;

import br.com.dsm.stickers.StickerGenerator;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

@Controller
@RequestMapping("/")
public class StickerController {

    private final StickerGenerator stickerGenerator;

    public StickerController(StickerGenerator stickerGenerator) {
        this.stickerGenerator = stickerGenerator;
    }

    @GetMapping
    public String index() {
        return "index";
    }

    @PostMapping("/generate")
    public String generateSticker(@RequestParam("imageUrl") String imageUrl,
                                  @RequestParam("stickerName") String stickerName,
                                  @RequestParam("text") String text,
                                  Model model) {
        try {
            InputStream inputStream = new URL(imageUrl).openStream();
            stickerGenerator.gerarStickers(inputStream, stickerName + ".png", text);
            model.addAttribute("message", "Figurinha gerada com sucesso!");
        } catch (IOException e) {
            e.printStackTrace();
            model.addAttribute("message", "Erro ao gerar a figurinha.");
        }
        return "index";
    }
}
