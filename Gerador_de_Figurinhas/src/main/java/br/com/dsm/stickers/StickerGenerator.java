package br.com.dsm.stickers;

import org.springframework.stereotype.Component;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

@Component
public class StickerGenerator {
    public void gerarStickers(InputStream inputStream, String nomeArquivo, String text) throws IOException {
        BufferedImage imagemOriginal = ImageIO.read(inputStream);

        int largura = imagemOriginal.getWidth();
        int altura = imagemOriginal.getHeight();
        int novaAltura = altura + 200;
        BufferedImage novaImagem = new BufferedImage(largura, novaAltura, BufferedImage.TYPE_INT_ARGB);

        Graphics2D graphics = (Graphics2D) novaImagem.getGraphics();
        graphics.drawImage(imagemOriginal, 0, 0, null);

        Font fonte = new Font(Font.SANS_SERIF, Font.BOLD, largura/10);
        graphics.setFont(fonte);
        graphics.setColor(Color.YELLOW);

        FontMetrics fontMetrics = graphics.getFontMetrics();
        int larguraTexto = fontMetrics.stringWidth(text);
        int posicaoHorizontalCentral = (largura - larguraTexto) / 2;

        graphics.drawString(text, posicaoHorizontalCentral, novaAltura - 80);

        ImageIO.write(novaImagem, "png", new File("saida/" + nomeArquivo));
    }
}
