<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sortable Table</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            cursor: pointer;
        }
    </style>
</head>
<body>
    <table id="forcePowersTable">
        <thead>
            <tr>
                <th onclick="sortTable(this.cellIndex)">Nome</th>
                <th onclick="sortTable(this.cellIndex)">Livello</th>
                <th onclick="sortTable(this.cellIndex)">Allineamento</th>
                <th onclick="sortTable(this.cellIndex)">Tempo di Lancio</th>
                <th onclick="sortTable(this.cellIndex)">Gittata</th>
                <th onclick="sortTable(this.cellIndex)">Durata</th>
                <th onclick="sortTable(this.cellIndex)">Concentrazione</th>
                <th onclick="sortTable(this.cellIndex)">Prerequisiti</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Influenzare la Mente (Affect Mind)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr style="color: red">
                <td>Affliggere (Affliction)</td>
                <td>2</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Lentezza (Slow)</td>
            </tr>
            <tr>
                <td>Animare Arma (Animate Weapon)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione bonus</td>
                <td>18 m</td>
                <td>1 minuto</td>
                <td>-</td>
                <td>Disarmare tramite la Forza (Force Disarm)</td>
            </tr>
            <tr style="color: red">
                <td>Armatura di Abeloth (Armor of Abeloth)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr style="color: blue">
                <td>Aura di Purezza (Aura of Purity)</td>
                <td>4</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 9 m)</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>Ristorare (Restoration)</td>
            </tr>
            <tr>
                <td>Aura di Vigore (Aura of Vigor)</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 9 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Valore (Valor)</td>
            </tr>
            <tr>
                <td>Intuizione da Battaglia (Battle Insight)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 round</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Meditazione da Battaglia (Battle Meditation)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 1.5 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Premonizione da Battaglia (Battle Precognition)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>8 ore</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Simbolo di Speranza (Beacon of Hope)</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Eroismo (Heroism)</td>
            </tr>
            <tr>
                <td>Ingannare Bestie (Beast Trick)</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>24 ore</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Scagliare Maledizioni (Bestow Curse)</td>
                <td>3</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Maledizione (Curse)</td>
            </tr>
            <tr>
                <td>Respiro Controllato (Breath Control)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>10 minuti</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Deflagrazione (Burst)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale (sfera di 1.5 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Accelerazione (Burst of Speed)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Evocare Fulmini (Call Lightning)</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Calmare Emozioni (Calm Emotions)</td>
                <td>2</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Percepire Emozioni (Sense Emotion)</td>
            </tr>
            <tr>
                <td>Strozzare (Choke)</td>
                <td>3</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Offuscare la Mente (Cloud Mind)</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>27 m</td>
                <td>1 minuto</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Manipolare la Mente (Coerce Mind)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 8 ore</td>
                <td>Concentrazione</td>
                <td>Influenzare la Mente (Affect Mind)</td>
            </tr>
            <tr>
                <td>Comprensione dei Linguaggi (Comprehend Speech)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Controllare il Dolore (Control Pain)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Corpo della Forza (Force Body)</td>
            </tr>
            <tr>
                <td>Convulsione (Convulsion)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Tremore (Tremor)</td>
            </tr>
            <tr>
                <td>Schiacciare (Crush)</td>
                <td>6</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Strozzare (Choke)</td>
            </tr>
            <tr>
                <td>Maledizione (Curse)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Denunciare (Denounce)</td>
            </tr>
            <tr>
                <td>Percepire Pericoli (Danger Sense)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione bonus</td>
                <td>Personale</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Aura Oscura (Dark Aura)</td>
                <td>3</td>
                <td>Oscuro</td>
                <td>1 azione bonus</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Stregare (Hex)</td>
            </tr>
            <tr>
                <td>Aculeo Oscuro (Dark Shear)</td>
                <td>2</td>
                <td>Oscuro</td>
                <td>1 azione bonus</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Tentacoli del Lato Oscuro (Dark Side Tendrils)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 3 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Oscurita&#39; (Darkness)</td>
                <td>2</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Campo di Morte (Death Field)</td>
                <td>8</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>27 m (cubo di 9 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Risucchio Vitale (Siphon Life)</td>
            </tr>
            <tr>
                <td>Denunciare (Denounce)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Distruggi Droide (Destroy Droid)</td>
                <td>7</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>36 m (cubo di 9 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Disabilitare Droide (Disable Droid)</td>
            </tr>
            <tr>
                <td>Disabilitare Droide (Disable Droid)</td>
                <td>4</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>27 m (cubo di 4.5 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Stordire Droide (Stun Droid)</td>
            </tr>
            <tr>
                <td>Disperdere la Forza (Disperse Force)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 reazione che puoi compiere se subisci danni di tipo: freddo, energia, fuoco, ioni, elettrici o sonori</td>
                <td>Personale</td>
                <td>1 round</td>
                <td>-</td>
                <td>Protezione dalle Lame (Saber Ward)</td>
            </tr>
            <tr>
                <td>Dominare Bestie (Dominate Beast)</td>
                <td>4</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Dominare Menti (Dominate Mind)</td>
                <td>5</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Dominare Bestie (Dominate Beast)</td>
            </tr>
            <tr>
                <td>Dominare Mostri (Dominate Monster)</td>
                <td>8</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 ora</td>
                <td>Concentrazione</td>
                <td>Dominare Menti (Dominate Mind)</td>
            </tr>
            <tr>
                <td>Risucchio Vitale (Drain Life)</td>
                <td>4</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Risucchiare Vitalita&#39; (Drain Vitality)</td>
            </tr>
            <tr>
                <td>Risucchiare Vitalita&#39; (Drain Vitality)</td>
                <td>2</td>
                <td>Oscuro</td>
                <td>1 azione tandard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Affaticare (Sap Vitality)</td>
            </tr>
            <tr>
                <td>Dun Moch</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione bonus</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Terremoto (Earthquake)</td>
                <td>8</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>150 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Eruzione (Eruption)</td>
            </tr>
            <tr>
                <td>Indebolire (Enfeeble)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Eruzione (Eruption)</td>
                <td>6</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Convulsione (Convulsion)</td>
            </tr>
            <tr>
                <td>Incutere Paura (Fear)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Retroazione (Feedback)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Barriera della Forza (Force Barrier)</td>
                <td>2</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>8 ore</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Cecita&#39;/Sordita&#39; della Forza (Force Blind/Deafen)</td>
                <td>2</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>1 minuto</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Bagliore della Forza (Force Blinding)</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>Personale (cono di 4.5 m)</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Sfocatura della Forza (Force Blur)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Maschera della Forza (Force Mask)</td>
            </tr>
            <tr>
                <td>Corpo della Forza (Force Body)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Dissolvere la Forza (Force Breach)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>36 m (cubo di 6 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Camuffamento della Forza (Force Camouflage)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 ora</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Catena di Fulmini della Forza (Force Chain Lightning)</td>
                <td>6</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>45 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Fulmini della Forza (Force Lightning)</td>
            </tr>
            <tr>
                <td>Occultamento della Forza (Force Concealment)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>24 ore</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Confusione della Forza (Force Confusion)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Disarmare tramite la Forza (Force Disarm)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Illuminazione della Forza (Force Enlightenment)</td>
                <td>2</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Fino ad 1 ora</td>
                <td>Concentrazione</td>
                <td>Guida (Guidance)</td>
            </tr>
            <tr>
                <td>Concentrazione della Forza (Force Focus)</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione bonus</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Tecnica della Forza (Force Technique)</td>
            </tr>
            <tr>
                <td>Irrorare la Forza (Force Imbuement)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione bonus</td>
                <td>A contatto</td>
                <td>1 minuto</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Immunita della Forza (Force Immunity)</td>
                <td>4</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Salto della Forza (Force Jump)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Slancio della Forza (Force Leap)</td>
            </tr>
            <tr>
                <td>Slancio della Forza (Force Leap)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione bonus</td>
                <td>Personale</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Fulmini della Forza (Force Lightning)</td>
                <td>3</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale (lineare di 30 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Shock</td>
            </tr>
            <tr>
                <td>Cono di Fulmini della Forza (Force Lightning Cone)</td>
                <td>7</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale (cono di 18 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Catena di Fulmini della Forza (Force Chain Lightning)</td>
            </tr>
            <tr>
                <td>Legame della Forza (Force Link)</td>
                <td>8</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Illimitata</td>
                <td>24 ore</td>
                <td>-</td>
                <td>Infusione della Forza (Force Meld)</td>
            </tr>
            <tr>
                <td>Maschera della Forza (Force Mask)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>1 ora</td>
                <td>-</td>
                <td>Trucco Mentale (Mind Trick)</td>
            </tr>
            <tr>
                <td>Infusione della Forza (Force Meld)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>1 ora</td>
                <td>-</td>
                <td>Bisbiglio della Forza (Force Whisper)</td>
            </tr>
            <tr>
                <td>Cura della Forza (Force Mend)</td>
                <td>7</td>
                <td>Chiaro</td>
                <td>1 minuto</td>
                <td>A contatto</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Proiettare la Forza (Force Project)</td>
                <td>7</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 giorno</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Propulsione della Forza (Force Propel)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Spinta/Attrazione della Forza (Force Push/Pull)</td>
            </tr>
            <tr>
                <td>Spinta/Attrazione della Forza (Force Push/Pull)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Deflessione della Forza (Force Deflect)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 reazione che puoi compiere se verresti colpito da un attacco a distanza</td>
                <td>Personale</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Deflettere con la Spada (Saber Reflect)</td>
            </tr>
            <tr>
                <td>Espulsione della Forza (Force Repulse)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 6 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Urlo della Forza (Force Scream)</td>
                <td>3</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 4.5 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Atterramento della Forza (Force Shunt)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Vista della Forza (Force Sight)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>Percepire la Forza (Sense Force)</td>
            </tr>
            <tr>
                <td>Tempesta della Forza (Force Storm)</td>
                <td>9</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>45 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Cono di Fulmini della Forza (Force Lightning Cone)</td>
            </tr>
            <tr>
                <td>Soppressione della Forza (Force Suppression)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Tecnica della Forza (Force Technique)</td>
                <td>0</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>Varia</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Lancio della Forza (Force Throw)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>27 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Spinta/Attrazione della Forza (Force Push/Pull)</td>
            </tr>
            <tr>
                <td>Trance della Forza (Force Trance)</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>10 minuti</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Visione della Forza (Force Vision)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 minuto</td>
                <td>18 m</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Arma della Forza (Force Weapon)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 azione bonus</td>
                <td>A contatto</td>
                <td>Fino ad 1 ora</td>
                <td>Concentrazione</td>
                <td>Irrorare la Forza (Force Imbuement)</td>
            </tr>
            <tr>
                <td>Bisbiglio della Forza (Force Whisper)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Liberta&#39; di Movimento (Freedom of Movement)</td>
                <td>4</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Donare Vita (Give Life)</td>
                <td>0</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Rampicante Afferrante (Grasping Vine)</td>
                <td>4</td>
                <td>Chiaro</td>
                <td>1 azione bonus</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Impeto Botanico (Plant Surge)</td>
            </tr>
            <tr>
                <td>Retroazione Potenziata (Greater Feedback)</td>
                <td>5</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Retroazione Migliorata (Improved Feedback)</td>
            </tr>
            <tr>
                <td>Cura Potenziata (Greater Heal)</td>
                <td>6</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Cura Migliorata (Improved Heal)</td>
            </tr>
            <tr>
                <td>Lancio della Spada Potenziato (Greater Saber Throw)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Lancio della Spada Migliorato (Improved Saber Throw)</td>
            </tr>
            <tr>
                <td>Guida (Guidance)</td>
                <td>0</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Allucinazione (Hallucination)</td>
                <td>2</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Cura Ferite (Heal)</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Eroismo (Heroism)</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Stregare (Hex)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione bonus</td>
                <td>27 m</td>
                <td>Fino ad 1 ora</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Orrore (Horror)</td>
                <td>3</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale (cono di 9 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Paura (Fear)</td>
            </tr>
            <tr>
                <td>Isteria (Hysteria)</td>
                <td>4</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Allucinazione (Hallucination)</td>
            </tr>
            <tr>
                <td>Meditazione da Battaglia Migliorata (Improved Battle Meditation)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 4.5 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Meditazione da Battaglia (Battle Meditation)</td>
            </tr>
            <tr>
                <td>Tentacoli del Lato Oscuro Migliorati (Improved Dark Side Tendrils)</td>
                <td>3</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>45 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Tentacoli del Lato Oscuro (Dark Side Tendrils)</td>
            </tr>
            <tr>
                <td>Retroazione Migliorata (Improved Feedback)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Retroazione (Feedback)</td>
            </tr>
            <tr>
                <td>Barriera della Forza Migliorata (Improved Force Barrier)</td>
                <td>5</td>
                <td>Chiaro</td>
                <td>10 minuti</td>
                <td>9 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Barriera della Forza (Force Barrier)</td>
            </tr>
            <tr>
                <td>Camuffamento della Forza Migliorato (Improved Force Camouflage)</td>
                <td>4</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Fino ad 1 minuto</td>
                <td>-</td>
                <td>Camuffamento della Forza (Force Camouflage)</td>
            </tr>
            <tr>
                <td>Immunita della Forza Migliorata (Improved Force Immunity)</td>
                <td>6</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 4.5 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Immunita della Forza (Force Immunity)</td>
            </tr>
            <tr>
                <td>Urlo della Forza Migliorato (Improved Force Scream)</td>
                <td>5</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 9 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Urlo della Forza (Force Scream)</td>
            </tr>
            <tr>
                <td>Cura Ferite Migliorato (Improved Heal)</td>
                <td>5</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Cura Ferite (Heal)</td>
            </tr>
            <tr>
                <td>Colpo in Fase Migliorato (Improved Phasestrike)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Colpo in Fase (Phasestrike)</td>
            </tr>
            <tr>
                <td>Camminata in Fase Migliorata (Improved Phasewalk)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione bonus</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Camminata in Fase (Phasewalk)</td>
            </tr>
            <tr>
                <td>Ripristinare Migliorato (Improved Restoration)</td>
                <td>5</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Ripristinare (Restoration)</td>
            </tr>
            <tr>
                <td>Ravvivare Migliorato (Improved Revitalize)</td>
                <td>7</td>
                <td>Chiaro</td>
                <td>10 minuti</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Ravvivare (Revitalize)</td>
            </tr>
            <tr>
                <td>Lancio della Spada Migliorato (Improved Saber Throw)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantaneo</td>
                <td>-</td>
                <td>Lancio della Spada (Saber Throw)</td>
            </tr>
            <tr>
                <td>Insanita&#39; (Insanity)</td>
                <td>5</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale (sfera di 9 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Orrore (Horror)</td>
            </tr>
            <tr>
                <td>Uccidere (Kill)</td>
                <td>9</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Rovina (Ruin)</td>
            </tr>
            <tr>
                <td>Velocita&#39; del Cavaliere (Knight Speed)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Accelerazione (Burst of Speed)</td>
            </tr>
            <tr>
                <td>Carica Fulminea (Lightning Charge)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Varia</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Localizzare Creatura (Locate Creature)</td>
                <td>4</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Localizzare Oggetto (Locate Object)</td>
            </tr>
            <tr>
                <td>Localizzare Oggetto (Locate Object)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Oscurita&#39; Esasperante (Maddening Darkness)</td>
                <td>8</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>45 m</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>Velo d&#39;Oscurita&#39; (Shroud of Darkness)</td>
            </tr>
            <tr>
                <td>Malessere (Malacia)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Trucco Mentale (Mind Trick)</td>
            </tr>
            <tr>
                <td>Animare di Massa (Mass Animation)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Animare Arma (Animate Weapon)</td>
            </tr>
            <tr>
                <td>Manipolare la Mente di Massa(Mass Coerce Mind)</td>
                <td>6</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>24 ore</td>
                <td>-</td>
                <td>Manipolare la Mente (Coerce Mind)</td>
            </tr>
            <tr>
                <td>Isteria di Massa (Mass Hysteria)</td>
                <td>9</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Isteria (Hysteria)</td>
            </tr>
            <tr>
                <td>Malessere di Massa (Mass Malacia)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>36 m (cubo di 9 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Malessere (Malacia)</td>
            </tr>
            <tr>
                <td>Meditazione da Battaglia Magistrale (Master Battle Meditation)</td>
                <td>9</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 9 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Meditazione da Battaglia Migliorata (Improved Battle Meditation)</td>
            </tr>
            <tr>
                <td>Retroazione Magistrale (Master Feedback)</td>
                <td>9</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>27 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Retroazione Potenziata (Greater Feedback)</td>
            </tr>
            <tr>
                <td>Barriera della Forza Magistrale (Master Force Barrier)</td>
                <td>8</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Barriera della Forza Migliorata (Improved Force Barrier)</td>
            </tr>
            <tr>
                <td>Immunita&#39; della Forza Magistrale (Master Force Immunity)</td>
                <td>8</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale (sfera con raggio di 3 m)</td>
                <td>Fino ad 1 ora</td>
                <td>Concentrazione</td>
                <td>Immunita&#39; della Forza Migliorata (Improved Force Immunity)</td>
            </tr>
            <tr>
                <td>Urlo della Forza Magistrale (Master Force Scream)</td>
                <td>8</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 18 m)</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Urlo della Forza Migliorato (Improved Force Scream)</td>
            </tr>
            <tr>
                <td>Cura Ferite Magistrale (Master Heal)</td>
                <td>9</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Cura Ferite Migliorato (Improved Heal)</td>
            </tr>
            <tr>
                <td>Malessere Magistrale (Master Malacia)</td>
                <td>6</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Malessere di Massa (Mass Malacia)</td>
            </tr>
            <tr>
                <td>Ravvivare Magistrale (Master Revitalize)</td>
                <td>9</td>
                <td>Chiaro</td>
                <td>1 ora</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Ravvivare Migliorato (Improved Revitalize)</td>
            </tr>
            <tr>
                <td>Lancio della Spada Magistrale (Master Saber Throw)</td>
                <td>7</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 27 m)</td>
                <td>Istantaneo</td>
                <td>-</td>
                <td>Lancio della Spada Potenziato (Greater Saber Throw)</td>
            </tr>
            <tr>
                <td>Velocita&#39; Magistrale (Master Speed)</td>
                <td>7</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Velocita&#39; del Cavaliere (Knight Speed)</td>
            </tr>
            <tr>
                <td>Vuoto Mentale (Mind Blank)</td>
                <td>8</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>24 ore</td>
                <td>-</td>
                <td>Trappola Mentale (Mind Trap)</td>
            </tr>
            <tr>
                <td>Prigione Mentale (Mind Prison)</td>
                <td>6</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Trappola Mentale (Mind Trap)</td>
            </tr>
            <tr>
                <td>Squarcio Mentale (Mind Spike)</td>
                <td>2</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 ora</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Trappola Mentale (Mind Trap)</td>
                <td>4</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Confusione della Forza (Force Confusion)</td>
            </tr>
            <tr>
                <td>Trucco Mentale (Mind Trick)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Morichro</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>1 ora</td>
                <td>-</td>
                <td>Offuscare la Mente (Cloud Mind)</td>
            </tr>
            <tr>
                <td>Carica Necrotica (Necrotic Charge)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Varia</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Tocco Necrotico (Necrotic Touch)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Colpo in Fase (Phasestrike)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione bonus</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Camminata in Fase (Phasewalk)</td>
                <td>2</td>
                <td>Universal</td>
                <td>1 azione bonus</td>
                <td>Personale</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Piaga (Plague)</td>
                <td>3</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Affliggere (Affliction)</td>
            </tr>
            <tr>
                <td>Impeto Botanico (Plant Surge)</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard od 8 ore</td>
                <td>45 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Premonizione (Precognition)</td>
                <td>9</td>
                <td>Universale</td>
                <td>1 minuto</td>
                <td>Personale</td>
                <td>8 ore</td>
                <td>-</td>
                <td>Percepire Pericoli (Danger Sense)</td>
            </tr>
            <tr>
                <td>Proiettare (Project)</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Carica Psichica (Psychic Charge)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Varia</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Psicometria (Psychometry)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 minuto</td>
                <td>Personale</td>
                <td>10 minuti</td>
                <td>-</td>
                <td>Telemetria (Telemetry)</td>
            </tr>
            <tr>
                <td>Ira (Rage)</td>
                <td>6</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Redarguire (Rebuke)</td>
                <td>0</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Rimuovere Maledizioni (Remove Curse)</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Salvataggio (Rescue)</td>
                <td>2</td>
                <td>Universale</td>
                <td>1 azione bonus</td>
                <td>9 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Resistenza (Resistance)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Ravvivare (Revitalize)</td>
                <td>5</td>
                <td>Chiaro</td>
                <td>1 minuto</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Risparmiare i Morenti (Spare the Dying)</td>
            </tr>
            <tr>
                <td>Rovina (Ruin)</td>
                <td>7</td>
                <td>Oscuro</td>
                <td>1 azione standared</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Ferire (Wound)</td>
            </tr>
            <tr>
                <td>Deflettere con la Spada (Saber Reflect)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 reazione che puoi compiere se subisci danni da un attacco a distanza</td>
                <td>Personale</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Lancio della Spada (Saber Throw)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Protezione dalle Lame (Saber Ward)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Santuario</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione bonus</td>
                <td>9 m</td>
                <td>1 minuto</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Affaticare (Sap Vitality)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Flagello (Scourge)</td>
                <td>6</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Piaga (Plague)</td>
            </tr>
            <tr>
                <td>Ribollire (Seethe)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Percepire Emozioni (Sense Emotion)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Percepire la Forza (Sense Force)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Disgiungere la Forza (Sever Force)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 reazione che puoi compiere quando vedi una creatura entro 18 m che lancia un potere della forza</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Vista delle Ombre (Shadow Sight)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Condividere Vita (Share Life)</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Donare Vita (Give Life)</td>
            </tr>
            <tr>
                <td>Shock</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>36 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Scudo Fulminante (Shocking Shield)</td>
                <td>4</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>10 Minuti</td>
                <td>-</td>
                <td>Shock</td>
            </tr>
            <tr>
                <td>Velo d&#39;Oscurita&#39; (Shroud of Darkness)</td>
                <td>4</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Oscurita&#39; (Darkness)</td>
            </tr>
            <tr>
                <td>Risucchio Vitale (Siphon Life)</td>
                <td>5</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Risucchio Vitale (Drain Life)</td>
            </tr>
            <tr>
                <td>Abilita&#39; Potenziata (Skill Empowerment)</td>
                <td>5</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Fino ad 1 ora</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Lentezza (Slow)</td>
                <td>0</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>4.5 m</td>
                <td>1 ora</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Caduta Lenta (Slow Descent)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 reazione che puoi compiere mentre tu od una creatura entro 18 m state cadendo</td>
                <td>18 m</td>
                <td>1 minuto</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Carica Sonica (Sonic Charge)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Varia</td>
                <td>1 round</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Trucco Sonoro (Sound Trick)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>1 minuto</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Risparmiare i Morenti (Spare the Dying)</td>
                <td>0</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Lama Spirituale (Spirit Blade)</td>
                <td>0</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Stasi (Stasis)</td>
                <td>5</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>27 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Stordire (Stun)</td>
            </tr>
            <tr>
                <td>Campo di Stasi (Stasis Field)</td>
                <td>8</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>36 m (cubo di 9 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Stasi (Stasis)</td>
            </tr>
            <tr>
                <td>Stordire (Stun)</td>
                <td>2</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Stordire Droide (Stun Droid)</td>
                <td>2</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Fulmine Controllato (Sustained Lightning)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Shock</td>
            </tr>
            <tr>
                <td>Telecinesi (Telekinesis)</td>
                <td>5</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>27 m</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>Lancio della Forza (Force Throw)</td>
            </tr>
            <tr>
                <td>Deflagrazione Telecinetica (Telekinetic Burst)</td>
                <td>6</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 18 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Tempesta Telecinetica (Telekinetic Storm)</td>
            </tr>
            <tr>
                <td>Scudo Telecinetico (Telekinetic Shield)</td>
                <td>3</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Animare Arma (Animate Weapon)</td>
            </tr>
            <tr>
                <td>Tempesta Telecinetica (Telekinetic Storm)</td>
                <td>3</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>Personale (raggio di 4.5 m)</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Turbolenza (Turbulence)</td>
            </tr>
            <tr>
                <td>Onda Telecinetica (Telekinetic Wave)</td>
                <td>8</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>45 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Deflagrazione Telecinetica (Telekinetic Burst)</td>
            </tr>
            <tr>
                <td>Telemetria (Telemetry)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 minuto</td>
                <td>A contatto</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Tremore (Tremor)</td>
                <td>1</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>3 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Deflagrazione (Burst)</td>
            </tr>
            <tr>
                <td>Visione del Vero (True Sight)</td>
                <td>6</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>1 ora</td>
                <td>-</td>
                <td>Vista della Forza (Force Sight)</td>
            </tr>
            <tr>
                <td>Turbolenza (Turbulence)</td>
                <td>0</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Valore (Valor)</td>
                <td>1</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>9 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>Resistenza (Resistance)</td>
            </tr>
            <tr>
                <td>Muro di Luce (Wall of Light)</td>
                <td>6</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>27 m</td>
                <td>Fino a 10 minuti</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Turbine (Whirlwind)</td>
                <td>7</td>
                <td>Universale</td>
                <td>1 azione standard</td>
                <td>90 m</td>
                <td>Fino ad 1 minuto</td>
                <td>Concentrazione</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Volonta' della Forza (Will of the Force)</td>
                <td>9</td>
                <td>Chiaro</td>
                <td>1 azione standard</td>
                <td>Personale</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Ferire (Wound)</td>
                <td>1</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Distruzione (Wrack)</td>
                <td>6</td>
                <td>Oscuro</td>
                <td>1 azione standard</td>
                <td>18 m</td>
                <td>Istantanea</td>
                <td>-</td>
                <td>Piaga (Plague)</td>
            </tr>
        </table>
    </tbody>
<script>
    function sortTable(n) {
        var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
        table = document.getElementById("forcePowersTable");
        switching = true;
        dir = "asc"; 
        while (switching) {
            switching = false;
            rows = table.rows;
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("TD")[n];
                y = rows[i + 1].getElementsByTagName("TD")[n];
                if (dir == "asc") {
                    if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                } else if (dir == "desc") {
                    if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
                switchcount++;
            } else {
                if (switchcount == 0 && dir == "asc") {
                    dir = "desc";
                    switching = true;
                }
            }
        }
    }
</script>

</body>
</html>
