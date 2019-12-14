<?php
require 'vendor/autoload.php';
 
use wikidata\Connection as Connection;
use wikidata\Wikidata as Wikidata;
 
try {
    // connect to the PostgreSQL database
    $pdo = Connection::get()->connect();
    //
    $wikiDB = new Wikidata($pdo);

    if(isset($_POST['search'])) {
    	$searchq = $_POST['search'];
        if (isset($_POST['checkbox1'])) {
            $s_wiki = $wikiDB->findByPK($searchq);
            $s_wiki = json_encode($s_wiki);
            $s_wiki = (array) json_decode($s_wiki);
            // Go ahead and do stuff because it is checked
        } else {
            $wikis = $wikiDB->findByAlias($searchq);
        }
    	//$keys = $wikiDB->findClaimKeys("Q42");
    	
    }

    //if(isset($_POST['w_id'])) {
    //	$w_id = $_POST['w_id'];
    	
    	//$keys = $wikiDB->findClaimKeys("Q42");
    //}


   //you could use: var_dump(pg_fetch_all($result));
    
    //var_dump($wikis);
    //var_dump($s_wiki);
    //var_dump(json_encode($keys));
    
} catch (\PDOException $e) {
    echo $e->getMessage();
}
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Joe's Here!</title>
        <link rel="stylesheet" href="bootstrap-4.3.1-dist/css/bootstrap.css">
        <link rel="stylesheet" href="bootstrap-4.3.1-dist/css/bootstrap-grid.css">
        <link rel="stylesheet" href="bootstrap-4.3.1-dist/js/bootstrap.js">

        <link rel="stylesheet" href="style.css">
    </head>
    <body>
	<div class="row">

	    <div class="col-sm-6">
            <div id="container">
   	            <p>Enter your query</p>
   	            <form name="form" method="post" action="wiki.php">
   	                <input name="search" type="text" size="30" maxlength="25" />
                    <input type="hidden" name="SubmitCheck" value="sent">
                    <input id="checkbox1" type="checkbox" name="checkbox1"> Query ID </input>
   	                <input name="submit" type="submit" value="Search" />
   	            </form> 
                <p>Previous query: <?php echo $searchq ?></p>
            </div>
        </div>
        <div class="col-sm-2">
            <h3>Joe's Wikidata Search Page</h3>
        </div>
        <div class="col-sm-4">
            <img width="70%" height="100" src="wikidata-logo.png">
        </div>

	</div>
	<div class="row">
	    <div id="l" class="col-sm-12">
   	        </div>
                <h1>Wiki List</h1>
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>Wikidata ID</th>
                            <th>English Label</th>
                            <th>Chinese Label</th>
                            <th>English Aliases</th>
                            <th>Chinese Aliases</th>
                            <th>English Description</th>
                            <th>Chinese Description</th>
                            <th>enwiki</th>
                            <th>zhwiki</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach ($wikis as $wiki) : ?>
                            <tr>
                                <td><?php echo htmlspecialchars($wiki['id']) ?></td>
                                <td><?php echo htmlspecialchars($wiki['en_label']) ?></td>
                                <td><?php echo htmlspecialchars($wiki['zh_label']) ?></td>
                                <td><?php echo htmlspecialchars($wiki['en_aliases']); ?></td>
                                <td><?php echo htmlspecialchars($wiki['zh_aliases']); ?></td>
                                <td><?php echo htmlspecialchars($wiki['en_desc']); ?></td>
                                <td><?php echo htmlspecialchars($wiki['zh_desc']); ?></td>
                                <td><?php echo htmlspecialchars($wiki['enwiki']); ?></td>
                                <td><?php echo htmlspecialchars($wiki['zhwiki']); ?></td>
                            </tr>
                        <?php endforeach; ?>

                    </tbody>
                </table>
	    </div>
	    <div id="s" class="col-sm-12">
   	        </div>
                <h1>Wiki Detail</h1>
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>Wikidata ID</th>
                            <th>English Label</th>
                            <th>Chinese Label</th>
                            <th>English Aliases</th>
                            <th>Chinese Aliases</th>
                            <th>English Description</th>
                            <th>Chinese Description</th>
                            <th>enwiki</th>
                            <th>zhwiki</th>
                        </tr>
                    </thead>
                    <tbody>

                            <tr>
                                <td><?php echo htmlspecialchars($s_wiki['id']) ?></td>
                                <td><?php echo htmlspecialchars($s_wiki['en_label']) ?></td>
                                <td><?php echo htmlspecialchars($s_wiki['zh_label']) ?></td>
                                <td><ul> <?php foreach (json_decode($s_wiki['en_aliases']) as $alias) : ?>
                                    <li><?php echo $alias ?></li>
                                <?php endforeach; ?></ul></td>
                                <td><ul> <?php foreach (json_decode($s_wiki['zh_aliases']) as $alias) : ?>
                                    <li><?php echo $alias ?></li>
                                <?php endforeach; ?></ul></td>
                                <td><?php echo htmlspecialchars($s_wiki['en_desc']); ?></td>
                                <td><?php echo htmlspecialchars($s_wiki['zh_desc']); ?></td>
                                <td><?php echo htmlspecialchars($s_wiki['enwiki']); ?></td>
                                <td><?php echo htmlspecialchars($s_wiki['zhwiki']); ?></td>
                            </tr>
                            <tr>
                                <td colspan="9"><ul> <?php foreach (json_decode($s_wiki['claims']) as $alias) : ?>
                                    <li><?php echo $alias ?></li>
                                <?php endforeach; ?></ul></td>
                            </tr>

                    </tbody>
                </table>

	    </div>
	</div>

    </body>
</html>
