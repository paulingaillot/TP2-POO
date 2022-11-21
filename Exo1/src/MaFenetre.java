import javax.swing.*;
import java.io.*;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

public class MaFenetre implements ActionListener {
    private JFrame f;
    private JButton[] bouton = new JButton[10];

    public MaFenetre() {
        f = new JFrame("Pigeon");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // comportement modifiable
        f.setSize(800, 700);
        // on place ici la definition de l'arbre de composants
        // frame.getContentPane().add(new MonDessin()); // forme exacte
        // ...
        // on termine generalement ainsi

        // Bouton

        for (int i = 0; i < 10; i++) {
            bouton[i] = new JButton();
            bouton[i].setBounds(100 + (i + 1) * 35, 460, 30, 30);
            bouton[i].setActionCommand("" + i);
            bouton[i].addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    int j = Integer.parseInt(e.getActionCommand());
                    Nourriture.Nourrituretab[j] = new Nourriture(j);
                    Nourriture.Nourrituretab[j].start();
                    System.out.println("Appui sur bouton");
                    Main.mafenetre.UpdatePigeon();
                }
            });
            f.add(bouton[i], 0);
        }

        try {
            JPanel panel = new JPanel();
            panel.setBounds(0, 0, 600, 550);
            BufferedImage img = ImageIO.read(new File("./Exo1/src/ressources/fenetre.png"));
            JLabel pic = new JLabel(new ImageIcon(img));
            panel.add(pic);
            f.add(panel);
            f.addComponentListener(null);
        } catch (Exception e) {
            e.printStackTrace();
        }

        f.setLayout(null);
        f.setVisible(true);
        // pour l'exemple

        f.validate();

        System.out.println(Thread.currentThread() + " en fin de MaFenetre()");
    }

    public void UpdateFood() {
        for (int i = 0; i < 10; i++) {
            if (Nourriture.Nourrituretab[i] != null) {

                try {
                    // f.removeAll();
                    // this.addBackGround();

                    bouton[i].setForeground(new Color(100, 255, 255));
                    bouton[i].setBounds(100 + (i + 1) * 35, 460, 30, 30);
                    Icon icon = new ImageIcon("./Exo1/src/ressources/graines.png");

                    bouton[i].setIcon(icon);
                    bouton[i].setBackground(new Color(100, 0, 255));
                    bouton[i].setVisible(true);
                    bouton[i].setEnabled(true);
                    f.add(bouton[i]).setForeground((new Color(255, 255, 255)));

                } catch (Exception e) {
                    e.printStackTrace();
                }
                f.validate();

            } else {
                bouton[i] = new JButton();
                bouton[i].setBounds(100 + (i + 1) * 35, 460, 30, 30);
                bouton[i].setActionCommand("" + i);
                bouton[i].addActionListener(new ActionListener() {
                    public void actionPerformed(ActionEvent e) {
                        int j = Integer.parseInt(e.getActionCommand());
                        Nourriture.Nourrituretab[j] = new Nourriture(j);
                        Nourriture.Nourrituretab[j].start();
                        System.out.println("Appui sur bouton");
                    }
                });
                f.add(bouton[i], 0);
                f.validate();
            }
        }
    }

    public void UpdatePigeon() {

        f.repaint();
        UpdateFood();
        f.validate();
        for (int i = 0; i < 10; i++) {
            if (Pigeon.Pigeontab[i] != null) {

                try {
                    // f.removeAll();
                    // this.addBackGround();
                    JPanel panel = new JPanel();
                    panel.setForeground(new Color(100, 255, 255));
                    panel.setBounds(100 + (i + 1) * 35, 415, 30, 30);
                    BufferedImage img = ImageIO.read(new File("./Exo1/src/ressources/pigeon.png"));
                    JLabel pic = new JLabel(new ImageIcon(img));
                    panel.add(pic);
                    f.add(panel).setForeground((new Color(255, 255, 255)));

                } catch (Exception e) {
                    e.printStackTrace();
                }
                f.validate();

            }
        }

    }

    @Override
    public void actionPerformed(ActionEvent e) {
    }
}