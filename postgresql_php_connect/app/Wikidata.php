<?php

namespace wikidata;

class Wikidata {
	private $pdo;

	public function __construct($pdo) {
		$this->pdo=$pdo;
	}


   	public function findByPK($id) {
		// prepare SELECT statement
   	    	$stmt = $this->pdo->prepare("
   	    			SELECT  
						data->'id' as id,
						data->'en_label' as en_label,
						data->'en_aliases' as en_aliases,
						data->'en_description' as en_desc,
						data->'enwiki' as enwiki,
						data->'zh_label' as zh_label,
						data->'zh_aliases' as zh_aliases,
						data->'zh_description' as zh_desc,
						data->'zhwiki' as zhwiki,
						data->'claims' as claims
   	    	        FROM wiki_bg
					WHERE data@>'{\"id\":\"$id\"}'");

   	    	// bind value to the :id parameter
   	    	//$stmt->bindValue(":id", $id);
   	    	
   	    	// execute the statement
   	    	$stmt->execute();
   	    	//$stmt->execute();

  	    	 // return the result set as an object
	    	return $stmt->fetchObject();
  	 }

	public function findByAlias($s) {
		$stmt = $this->pdo->query("
					SELECT
						data->'id' as id,
						data->'en_label' as en_label,
						data->'en_aliases' as en_aliases,
						data->'en_description' as en_desc,
						data->'enwiki' as enwiki,
						data->'zh_label' as zh_label,
						data->'zh_aliases' as zh_aliases,
						data->'zh_description' as zh_desc,
						data->'zhwiki' as zhwiki
					FROM wiki_bg 
					WHERE data->>'en_aliases' ILIKE '%$s%' OR 
						  data->>'zh_aliases' ILIKE '%$s%'
				");
		$items = [];
		foreach ($stmt as $row){
			//echo $row['lbl'] . "\n";
			$items[] = [
				'id' => $row['id'],
				'en_label' => $row['en_label'],
				'zh_label' => $row['zh_label'],
				'en_aliases' => json_decode($row['en_aliases'])[0],
				'zh_aliases' => json_decode($row['zh_aliases'])[0],
				'en_desc' => $row['en_desc'],
				'zh_desc' => $row['zh_desc'],
				'enwiki' => $row['enwiki'],
				'zhwiki' => $row['zhwiki']
			];
		}
		return $items;
	}

	public function findClaimKeys($id) {

						//data->'claims' as key
		$stmt = $this->pdo->query("SELECT
						jsonb_object_keys(data->'claims') as key
					   FROM bg
					   WHERE data@>'{\"id\":\"$id\"}'");
		$stmt->execute();
		$stmt->fetchColumn();
		$props = [];
		foreach ($stmt as $row){
			array_push($props,$row);
		}
		return $props; 
			
	}
	       	
}



