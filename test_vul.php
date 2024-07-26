<?php
try {
    $dbh->beginTransaction();

    // Prepare the update of the main table
    $qmark_pairs = array();
    foreach ($data as $key => $val) {
        $qmark_pairs[] = $key . " = ? ";
    }
    $query = "UPDATE grants SET " . implode(",", $qmark_pairs) . " WHERE grant_id = {$gr_id}";
    $stmt = $dbh->prepare($query);
    $stmt->execute(array_values($data));

    // Delete old athenz domains/record types associations
    $query_del_ad = "DELETE FROM grants_athenzDomain WHERE grant_id = {$gr_id}";
    $stmt = $dbh->prepare($query_del_ad);
    $stmt->execute();

    $dbh->commit();
} catch (Exception $e) {
    $dbh->rollBack();
    throw $e;
}
?>
